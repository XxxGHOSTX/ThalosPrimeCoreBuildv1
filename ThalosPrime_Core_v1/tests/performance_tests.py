"""
Thalos Prime - Performance Tests
Copyright (c) 2026 Tony Ray Macier III
"""

import unittest
import numpy as np
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from core.sbi_engine import SBIEngine
from core.matrix_codex import MatrixCodex, CodexConfig
from core.tensor_lib import SynapticTensor, TensorBroadcaster
from pipelines.reasoning_pipeline import ReasoningPipeline


class TestSBIEnginePerformance(unittest.TestCase):
    def setUp(self):
        self.engine = SBIEngine()

    def test_intent_dissection_latency(self):
        """Test that intent dissection completes within acceptable time"""
        test_input = "This is a test query for performance evaluation"

        start_time = time.time()
        for _ in range(100):
            result = self.engine.process_input(test_input)
        elapsed = time.time() - start_time

        avg_latency = elapsed / 100
        self.assertLess(avg_latency, 0.1, f"Average latency {avg_latency:.4f}s exceeds 0.1s")
        print(f"Average intent dissection latency: {avg_latency*1000:.2f}ms")


class TestMatrixCodexPerformance(unittest.TestCase):
    def setUp(self):
        # Smaller model for performance testing
        config = CodexConfig(
            num_layers=12,
            num_heads=16,
            hidden_dim=1024,
            ff_dim=4096
        )
        self.codex = MatrixCodex(config)

    def test_forward_pass_throughput(self):
        """Test forward pass throughput"""
        batch_size = 8
        seq_len = 128
        input_ids = np.random.randint(0, 50000, size=(batch_size, seq_len))

        start_time = time.time()
        logits = self.codex.forward(input_ids)
        elapsed = time.time() - start_time

        tokens_per_second = (batch_size * seq_len) / elapsed
        print(f"Throughput: {tokens_per_second:.0f} tokens/second")
        self.assertGreater(tokens_per_second, 1000, "Throughput below 1000 tokens/s")


class TestTensorPerformance(unittest.TestCase):
    def setUp(self):
        self.tensor = SynapticTensor(np.random.randn(64, 10000, 128))
        self.broadcaster = TensorBroadcaster()

    def test_broadcast_performance(self):
        """Test tensor broadcast operation performance"""
        tensor_b = SynapticTensor(np.random.randn(64, 10000, 128))

        start_time = time.time()
        for _ in range(10):
            result = self.broadcaster.broadcast_multiply(self.tensor, tensor_b)
        elapsed = time.time() - start_time

        avg_time = elapsed / 10
        print(f"Average broadcast time: {avg_time*1000:.2f}ms")
        self.assertLess(avg_time, 0.5, "Broadcast operation too slow")

    def test_memory_efficiency(self):
        """Test memory usage stays within bounds"""
        import psutil
        import os

        process = psutil.Process(os.getpid())
        mem_before = process.memory_info().rss / 1024 / 1024  # MB

        # Create and process large tensors
        tensors = []
        for _ in range(10):
            t = SynapticTensor(np.random.randn(32, 5000, 64))
            normalized = t.normalize()
            pooled = normalized.spatial_pooling(pool_size=2)
            tensors.append(pooled)

        mem_after = process.memory_info().rss / 1024 / 1024  # MB
        mem_increase = mem_after - mem_before

        print(f"Memory increase: {mem_increase:.1f} MB")
        self.assertLess(mem_increase, 5000, "Memory usage exceeds 5GB")


class TestPipelinePerformance(unittest.TestCase):
    def setUp(self):
        self.reasoning = ReasoningPipeline()

    def test_end_to_end_latency(self):
        """Test complete reasoning pipeline latency"""
        input_data = np.random.randn(50, 512)
        bio_state = np.random.randn(64, 1000, 64)

        start_time = time.time()
        for _ in range(10):
            result = self.reasoning.reason(input_data, bio_state)
        elapsed = time.time() - start_time

        avg_latency = elapsed / 10
        print(f"Average reasoning latency: {avg_latency*1000:.2f}ms")
        self.assertLess(avg_latency, 1.0, "Reasoning latency exceeds 1 second")


class TestMetabolicEfficiency(unittest.TestCase):
    def test_cpu_utilization(self):
        """Test CPU utilization stays within reasonable bounds"""
        import psutil

        # Measure CPU during intensive operation
        cpu_percent_start = psutil.cpu_percent(interval=1)

        # Simulate intensive workload
        for _ in range(1000):
            _ = np.random.randn(100, 100) @ np.random.randn(100, 100)

        cpu_percent_end = psutil.cpu_percent(interval=1)

        print(f"CPU utilization: {cpu_percent_end:.1f}%")
        self.assertLess(cpu_percent_end, 95, "CPU utilization too high")


if __name__ == '__main__':
    # Run with verbose output
    unittest.main(verbosity=2)
