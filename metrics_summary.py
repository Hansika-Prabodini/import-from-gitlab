#!/usr/bin/env python3
"""
Aggregate Metrics Summary Script

This script provides a comprehensive overview of all metrics and KPIs tracked
in the llm-benchmarking-py project. It aggregates test results, benchmark data,
and coverage information to provide a holistic view of project health.

Usage:
    python metrics_summary.py
    or
    poetry run python metrics_summary.py
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


class MetricsCollector:
    """Collects and aggregates metrics from various sources"""

    def __init__(self):
        self.results: Dict[str, any] = {}
        self.project_root = Path(__file__).parent

    def run_command(self, command: List[str]) -> tuple[int, str, str]:
        """
        Run a shell command and capture output.
        
        Returns:
            Tuple of (return_code, stdout, stderr)
        """
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                cwd=self.project_root
            )
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            return 1, "", str(e)

    def collect_test_metrics(self) -> Dict[str, any]:
        """Run pytest and collect test pass/fail metrics"""
        print("📊 Collecting test metrics...")
        
        returncode, stdout, stderr = self.run_command([
            "poetry", "run", "pytest", "--benchmark-skip", 
            "-v", "--tb=no", "tests/"
        ])
        
        metrics = {
            "status": "success" if returncode == 0 else "failure",
            "return_code": returncode,
        }
        
        # Parse test results from output
        if "passed" in stdout or "passed" in stderr:
            output = stdout + stderr
            # Extract test counts
            for line in output.split('\n'):
                if 'passed' in line.lower():
                    metrics["summary"] = line.strip()
                    break
        
        return metrics

    def collect_benchmark_metrics(self) -> Dict[str, any]:
        """Run pytest benchmarks and collect performance metrics"""
        print("⚡ Collecting benchmark metrics...")
        
        returncode, stdout, stderr = self.run_command([
            "poetry", "run", "pytest", "--benchmark-only",
            "--benchmark-columns=min,max,mean,median,ops",
            "tests/"
        ])
        
        metrics = {
            "status": "success" if returncode == 0 else "failure",
            "return_code": returncode,
        }
        
        # Parse benchmark summary
        if "benchmark:" in stdout:
            output_lines = stdout.split('\n')
            benchmark_section = []
            in_benchmark = False
            
            for line in output_lines:
                if "benchmark:" in line.lower():
                    in_benchmark = True
                if in_benchmark:
                    benchmark_section.append(line)
                    if line.strip().startswith("==="):
                        break
            
            metrics["summary"] = "\n".join(benchmark_section) if benchmark_section else "Benchmarks completed"
        
        return metrics

    def collect_coverage_metrics(self) -> Dict[str, any]:
        """Run pytest with coverage and collect coverage metrics"""
        print("🎯 Collecting coverage metrics...")
        
        returncode, stdout, stderr = self.run_command([
            "poetry", "run", "pytest", "--cov=src", 
            "--cov-report=term-missing", "--benchmark-skip",
            "tests/"
        ])
        
        metrics = {
            "status": "success" if returncode == 0 else "failure",
            "return_code": returncode,
        }
        
        # Parse coverage percentage
        output = stdout + stderr
        for line in output.split('\n'):
            if "TOTAL" in line:
                parts = line.split()
                if len(parts) >= 4:
                    try:
                        coverage_pct = parts[-1].rstrip('%')
                        metrics["coverage_percentage"] = float(coverage_pct)
                        metrics["coverage_line"] = line.strip()
                    except (ValueError, IndexError):
                        pass
        
        return metrics

    def collect_module_info(self) -> Dict[str, any]:
        """Collect information about modules and their test coverage"""
        print("📦 Collecting module information...")
        
        src_modules = list((self.project_root / "src" / "llm_benchmark").glob("*/"))
        test_modules = list((self.project_root / "tests" / "llm_benchmark").glob("*/"))
        
        src_module_names = {m.name for m in src_modules if m.is_dir() and m.name != "__pycache__"}
        test_module_names = {m.name for m in test_modules if m.is_dir() and m.name != "__pycache__"}
        
        # Find modules with/without tests
        tested_modules = src_module_names & test_module_names
        untested_modules = src_module_names - test_module_names
        
        # Count test files
        test_file_count = len(list((self.project_root / "tests").rglob("test_*.py")))
        src_file_count = len(list((self.project_root / "src").rglob("*.py"))) - \
                        len(list((self.project_root / "src").rglob("__init__.py")))
        
        return {
            "total_modules": len(src_module_names),
            "tested_modules": list(sorted(tested_modules)),
            "untested_modules": list(sorted(untested_modules)),
            "test_file_count": test_file_count,
            "source_file_count": src_file_count,
            "modules_with_tests": len(tested_modules),
            "modules_without_tests": len(untested_modules),
        }

    def generate_report(self) -> str:
        """Generate a comprehensive metrics report"""
        report_lines = []
        
        # Header
        report_lines.append("=" * 80)
        report_lines.append("LLM BENCHMARKING PROJECT - METRICS SUMMARY")
        report_lines.append("=" * 80)
        report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append("")
        
        # Module Coverage
        if "modules" in self.results:
            modules = self.results["modules"]
            report_lines.append("📦 MODULE COVERAGE")
            report_lines.append("-" * 80)
            report_lines.append(f"Total Modules: {modules['total_modules']}")
            report_lines.append(f"Modules with Tests: {modules['modules_with_tests']} / {modules['total_modules']}")
            
            coverage_pct = (modules['modules_with_tests'] / modules['total_modules'] * 100) if modules['total_modules'] > 0 else 0
            report_lines.append(f"Module Test Coverage: {coverage_pct:.1f}%")
            report_lines.append(f"\nTested Modules: {', '.join(modules['tested_modules'])}")
            
            if modules['untested_modules']:
                report_lines.append(f"⚠️  Untested Modules: {', '.join(modules['untested_modules'])}")
            
            report_lines.append(f"\nTest Files: {modules['test_file_count']}")
            report_lines.append(f"Source Files: {modules['source_file_count']}")
            report_lines.append("")
        
        # Test Results
        if "tests" in self.results:
            tests = self.results["tests"]
            report_lines.append("✅ UNIT TEST RESULTS")
            report_lines.append("-" * 80)
            report_lines.append(f"Status: {tests['status'].upper()}")
            if "summary" in tests:
                report_lines.append(f"Summary: {tests['summary']}")
            report_lines.append("")
        
        # Code Coverage
        if "coverage" in self.results:
            coverage = self.results["coverage"]
            report_lines.append("🎯 CODE COVERAGE")
            report_lines.append("-" * 80)
            if "coverage_percentage" in coverage:
                pct = coverage["coverage_percentage"]
                status = "✅ Excellent" if pct >= 90 else "⚠️  Good" if pct >= 80 else "❌ Needs Improvement"
                report_lines.append(f"Coverage: {pct}% - {status}")
                
                if "coverage_line" in coverage:
                    report_lines.append(f"Details: {coverage['coverage_line']}")
            else:
                report_lines.append("Coverage data not available")
            report_lines.append("")
        
        # Benchmark Results
        if "benchmarks" in self.results:
            benchmarks = self.results["benchmarks"]
            report_lines.append("⚡ PERFORMANCE BENCHMARKS")
            report_lines.append("-" * 80)
            report_lines.append(f"Status: {benchmarks['status'].upper()}")
            if "summary" in benchmarks:
                report_lines.append(benchmarks['summary'])
            report_lines.append("")
        
        # Overall Health Score
        report_lines.append("📈 OVERALL PROJECT HEALTH")
        report_lines.append("-" * 80)
        
        health_score = 0
        max_score = 0
        
        # Calculate health score based on available metrics
        if "tests" in self.results:
            max_score += 25
            if self.results["tests"]["status"] == "success":
                health_score += 25
                report_lines.append("✅ All tests passing (+25 points)")
            else:
                report_lines.append("❌ Some tests failing (+0 points)")
        
        if "coverage" in self.results and "coverage_percentage" in self.results["coverage"]:
            max_score += 25
            cov_pct = self.results["coverage"]["coverage_percentage"]
            if cov_pct >= 90:
                health_score += 25
                report_lines.append(f"✅ Excellent coverage: {cov_pct}% (+25 points)")
            elif cov_pct >= 80:
                health_score += 20
                report_lines.append(f"⚠️  Good coverage: {cov_pct}% (+20 points)")
            else:
                health_score += 10
                report_lines.append(f"❌ Low coverage: {cov_pct}% (+10 points)")
        
        if "modules" in self.results:
            max_score += 25
            modules = self.results["modules"]
            if modules["modules_without_tests"] == 0:
                health_score += 25
                report_lines.append("✅ All modules tested (+25 points)")
            else:
                partial_score = int(25 * (modules["modules_with_tests"] / modules["total_modules"]))
                health_score += partial_score
                report_lines.append(f"⚠️  {modules['modules_without_tests']} untested module(s) (+{partial_score} points)")
        
        if "benchmarks" in self.results:
            max_score += 25
            if self.results["benchmarks"]["status"] == "success":
                health_score += 25
                report_lines.append("✅ All benchmarks completed (+25 points)")
            else:
                report_lines.append("❌ Benchmark issues (+0 points)")
        
        if max_score > 0:
            health_percentage = (health_score / max_score) * 100
            report_lines.append("")
            report_lines.append(f"Overall Health Score: {health_score}/{max_score} ({health_percentage:.1f}%)")
            
            if health_percentage >= 90:
                report_lines.append("Status: 🌟 EXCELLENT - Project is in great shape!")
            elif health_percentage >= 75:
                report_lines.append("Status: ✅ GOOD - Minor improvements recommended")
            elif health_percentage >= 60:
                report_lines.append("Status: ⚠️  FAIR - Some issues need attention")
            else:
                report_lines.append("Status: ❌ POOR - Significant improvements needed")
        
        report_lines.append("")
        report_lines.append("=" * 80)
        
        # Recommendations
        report_lines.append("\n💡 RECOMMENDATIONS")
        report_lines.append("-" * 80)
        
        recommendations = []
        
        if "modules" in self.results and self.results["modules"]["untested_modules"]:
            recommendations.append(f"• Add tests for: {', '.join(self.results['modules']['untested_modules'])}")
        
        if "coverage" in self.results and "coverage_percentage" in self.results["coverage"]:
            if self.results["coverage"]["coverage_percentage"] < 90:
                recommendations.append(f"• Increase code coverage to 90%+ (currently {self.results['coverage']['coverage_percentage']}%)")
        
        if "tests" in self.results and self.results["tests"]["status"] != "success":
            recommendations.append("• Fix failing tests")
        
        if not recommendations:
            recommendations.append("• Keep up the great work! Consider adding more edge case tests.")
        
        for rec in recommendations:
            report_lines.append(rec)
        
        report_lines.append("")
        report_lines.append("=" * 80)
        report_lines.append("For detailed metrics, see: METRICS_ANALYSIS.md")
        report_lines.append("=" * 80)
        
        return "\n".join(report_lines)

    def run(self) -> None:
        """Run all metrics collection and generate report"""
        print("\n" + "=" * 80)
        print("COLLECTING PROJECT METRICS")
        print("=" * 80 + "\n")
        
        # Collect all metrics
        self.results["modules"] = self.collect_module_info()
        self.results["tests"] = self.collect_test_metrics()
        self.results["coverage"] = self.collect_coverage_metrics()
        self.results["benchmarks"] = self.collect_benchmark_metrics()
        
        # Generate and display report
        print("\n" + "=" * 80)
        print("GENERATING REPORT")
        print("=" * 80 + "\n")
        
        report = self.generate_report()
        print(report)
        
        # Save report to file
        report_file = self.project_root / "METRICS_REPORT.txt"
        with open(report_file, "w") as f:
            f.write(report)
        
        print(f"\n📄 Report saved to: {report_file}")


def main():
    """Main entry point"""
    try:
        collector = MetricsCollector()
        collector.run()
    except KeyboardInterrupt:
        print("\n\n❌ Metrics collection interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error during metrics collection: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
