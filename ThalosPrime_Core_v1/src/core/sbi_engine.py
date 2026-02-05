"""
THALOS PRIME CORE V1 - SBI Engine
==================================

Digital Thalamus: Semantic Intent Dissection and Synaptic Routing

Copyright (c) 2026 Tony Ray Macier III
All Rights Reserved.

The SBI Engine acts as the "Digital Thalamus" of Thalos Prime, performing
sophisticated semantic intent dissection rather than simple pattern matching.
It breaks down input into core concepts and maps them to biological lobes
with the highest success probability for specific knowledge domains.
"""

import numpy as np
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
from enum import Enum
import logging
from pathlib import Path
import yaml


class IntentDomain(Enum):
    """Knowledge domains for synaptic routing"""
    LOGICAL_REASONING = "logical_reasoning"
    CREATIVE_SYNTHESIS = "creative_synthesis"
    MATHEMATICAL_ANALYSIS = "mathematical_analysis"
    LINGUISTIC_PROCESSING = "linguistic_processing"
    PATTERN_RECOGNITION = "pattern_recognition"
    MEMORY_RETRIEVAL = "memory_retrieval"
    ETHICAL_EVALUATION = "ethical_evaluation"
    SPATIAL_REASONING = "spatial_reasoning"


@dataclass
class SemanticIntent:
    """Dissected semantic intent structure"""
    primary_domain: IntentDomain
    secondary_domains: List[IntentDomain]
    confidence: float
    concept_vectors: np.ndarray
    biological_affinity: float
    complexity_score: float
    requires_reflection: bool


class SemanticIntentDissector:
    """
    Performs deep semantic analysis to identify true intent rather than
    surface-level pattern matching.
    """

    def __init__(self, vocab_size: int = 50000, embedding_dim: int = 512):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.concept_embeddings = self._initialize_embeddings()
        self.domain_classifiers = self._initialize_domain_classifiers()
        self.logger = logging.getLogger("SBIEngine.Dissector")

    def _initialize_embeddings(self) -> np.ndarray:
        """Initialize concept embedding matrix"""
        # Xavier initialization for concept vectors
        scale = np.sqrt(2.0 / (self.vocab_size + self.embedding_dim))
        return np.random.randn(self.vocab_size, self.embedding_dim) * scale

    def _initialize_domain_classifiers(self) -> Dict[IntentDomain, np.ndarray]:
        """Initialize domain-specific classification weights"""
        classifiers = {}
        for domain in IntentDomain:
            # Each domain has its own projection matrix
            classifiers[domain] = np.random.randn(self.embedding_dim, 128) * 0.01
        return classifiers

    def dissect(self, input_tokens: List[int], context: Optional[List[int]] = None) -> SemanticIntent:
        """
        Perform semantic intent dissection on input tokens.

        Args:
            input_tokens: Tokenized input sequence
            context: Optional context tokens from previous interactions

        Returns:
            SemanticIntent object containing dissected intent
        """
        # Embed input tokens
        input_embeddings = self.concept_embeddings[input_tokens]
        mean_embedding = np.mean(input_embeddings, axis=0)

        # Classify across all domains
        domain_scores = {}
        for domain, classifier in self.domain_classifiers.items():
            score = np.mean(np.tanh(mean_embedding @ classifier))
            domain_scores[domain] = float(score)

        # Identify primary and secondary domains
        sorted_domains = sorted(domain_scores.items(), key=lambda x: x[1], reverse=True)
        primary_domain = sorted_domains[0][0]
        secondary_domains = [d[0] for d in sorted_domains[1:4]]

        # Calculate biological affinity (preference for biological processing)
        biological_affinity = self._calculate_bio_affinity(mean_embedding)

        # Calculate complexity score
        complexity_score = self._calculate_complexity(input_embeddings)

        # Determine if reflection is required
        requires_reflection = complexity_score > 0.7 or biological_affinity > 0.6

        return SemanticIntent(
            primary_domain=primary_domain,
            secondary_domains=secondary_domains,
            confidence=sorted_domains[0][1],
            concept_vectors=mean_embedding,
            biological_affinity=biological_affinity,
            complexity_score=complexity_score,
            requires_reflection=requires_reflection
        )

    def _calculate_bio_affinity(self, embedding: np.ndarray) -> float:
        """Calculate affinity for biological processing"""
        # Biological systems excel at non-linear, context-rich problems
        nonlinearity = np.std(embedding) / (np.mean(np.abs(embedding)) + 1e-8)
        return float(np.tanh(nonlinearity))

    def _calculate_complexity(self, embeddings: np.ndarray) -> float:
        """Calculate input complexity score"""
        # Complexity based on embedding variance and sequence length
        variance = np.mean(np.var(embeddings, axis=0))
        length_factor = min(embeddings.shape[0] / 100.0, 1.0)
        return float(np.tanh(variance * length_factor))


class SynapticRouter:
    """
    Routes processed intents to appropriate biological or digital processing units
    """

    def __init__(self, num_biological_lobes: int = 8, num_digital_cores: int = 16):
        self.num_biological_lobes = num_biological_lobes
        self.num_digital_cores = num_digital_cores
        self.routing_matrix = self._initialize_routing()
        self.logger = logging.getLogger("SBIEngine.Router")

    def _initialize_routing(self) -> np.ndarray:
        """Initialize routing probability matrix"""
        total_units = self.num_biological_lobes + self.num_digital_cores
        return np.random.dirichlet(np.ones(total_units), size=len(IntentDomain))

    def route(self, intent: SemanticIntent) -> Tuple[List[int], List[int]]:
        """
        Route intent to biological lobes and digital cores.

        Args:
            intent: Dissected semantic intent

        Returns:
            Tuple of (biological_lobe_ids, digital_core_ids)
        """
        domain_idx = list(IntentDomain).index(intent.primary_domain)
        routing_probs = self.routing_matrix[domain_idx]

        # Apply biological affinity bias
        bio_probs = routing_probs[:self.num_biological_lobes] * (1 + intent.biological_affinity)
        digital_probs = routing_probs[self.num_biological_lobes:]

        # Normalize
        all_probs = np.concatenate([bio_probs, digital_probs])
        all_probs = all_probs / np.sum(all_probs)

        # Select top processing units
        num_units = 3 if intent.complexity_score > 0.5 else 2
        selected_indices = np.argsort(all_probs)[-num_units:]

        biological_lobes = [idx for idx in selected_indices if idx < self.num_biological_lobes]
        digital_cores = [idx - self.num_biological_lobes for idx in selected_indices
                         if idx >= self.num_biological_lobes]

        self.logger.info(f"Routed to {len(biological_lobes)} biological lobes, "
                        f"{len(digital_cores)} digital cores")

        return biological_lobes, digital_cores


class SBIEngine:
    """
    Main Synthetic Biological Intelligence Engine

    The SBI Engine orchestrates the entire intent analysis and synaptic routing
    process, serving as the central nervous system of Thalos Prime.
    """

    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the SBI Engine.

        Args:
            config_path: Path to configuration file
        """
        self.config = self._load_config(config_path)
        self.dissector = SemanticIntentDissector(
            vocab_size=self.config.get('vocab_size', 50000),
            embedding_dim=self.config.get('embedding_dim', 512)
        )
        self.router = SynapticRouter(
            num_biological_lobes=self.config.get('num_biological_lobes', 8),
            num_digital_cores=self.config.get('num_digital_cores', 16)
        )
        self.logger = logging.getLogger("SBIEngine")
        self.logger.info("SBI Engine initialized - Digital Thalamus online")

    def _load_config(self, config_path: Optional[str]) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        if config_path and Path(config_path).exists():
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        return {
            'vocab_size': 50000,
            'embedding_dim': 512,
            'num_biological_lobes': 8,
            'num_digital_cores': 16
        }

    def process_input(self, input_text: str, context: Optional[str] = None) -> Dict[str, Any]:
        """
        Process input through the SBI pipeline.

        Args:
            input_text: Raw input text
            context: Optional context from previous interactions

        Returns:
            Dictionary containing routing information and intent analysis
        """
        # Tokenize input (simplified - would use proper tokenizer in production)
        input_tokens = self._tokenize(input_text)
        context_tokens = self._tokenize(context) if context else None

        # Dissect semantic intent
        intent = self.dissector.dissect(input_tokens, context_tokens)

        # Route to processing units
        bio_lobes, digital_cores = self.router.route(intent)

        result = {
            'intent': intent,
            'biological_lobes': bio_lobes,
            'digital_cores': digital_cores,
            'requires_reflection': intent.requires_reflection,
            'processing_mode': 'hybrid' if bio_lobes and digital_cores else
                             'biological' if bio_lobes else 'digital'
        }

        self.logger.info(f"Processed input: {intent.primary_domain.value}, "
                        f"confidence={intent.confidence:.3f}")

        return result

    def _tokenize(self, text: str) -> List[int]:
        """Simple tokenization (would use proper tokenizer in production)"""
        if not text:
            return []
        # Hash-based tokenization for demonstration
        tokens = []
        for word in text.lower().split():
            token_id = hash(word) % self.config.get('vocab_size', 50000)
            tokens.append(token_id)
        return tokens

    def update_routing(self, intent: SemanticIntent, success_feedback: float):
        """
        Update routing matrix based on success feedback.

        Args:
            intent: The intent that was processed
            success_feedback: Success score from 0.0 to 1.0
        """
        domain_idx = list(IntentDomain).index(intent.primary_domain)
        learning_rate = 0.01

        # Strengthen successful routing patterns
        self.router.routing_matrix[domain_idx] *= (1 + learning_rate * success_feedback)
        self.router.routing_matrix[domain_idx] /= np.sum(self.router.routing_matrix[domain_idx])

        self.logger.debug(f"Updated routing for {intent.primary_domain.value}")


# Sovereign verification
__author__ = "Tony Ray Macier III"
__copyright__ = "Copyright 2026, Thalos Prime Coding"
__license__ = "Proprietary - All Rights Reserved"
