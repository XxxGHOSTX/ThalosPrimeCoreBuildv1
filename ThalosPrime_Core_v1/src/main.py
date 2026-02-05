"""
THALOS PRIME CORE V1 - Main Entry Point
========================================

Sovereign Launch Sequence

Copyright (c) 2026 Tony Ray Macier III
All Rights Reserved.

This is the main entry point for the Thalos Prime Synthetic Biological
Intelligence system. It orchestrates the initialization and operation of
all subsystems including the Matrix Codex, biological interfaces, and
the Machine World GUI.
"""

import sys
import logging
from pathlib import Path
import argparse

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from core.sbi_engine import SBIEngine
from core.matrix_codex import MatrixCodex, CodexConfig
from pipelines.input_pipeline import InputPipeline
from pipelines.reasoning_pipeline import ReasoningPipeline
from pipelines.output_pipeline import OutputPipeline
from security.access_control import AccessControl
from gui.window_manager import WindowManager
from gui.input_output_ui import InputOutputUI
from gui.settings_toolbar import SettingsToolbar
from gui.status_tab import StatusTab
from integration.messaging import MessageBus
from integration.monitoring import SystemMonitor

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('thalos_prime.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ThalosPrime")


class ThalosPrimeCore:
    """
    Main Thalos Prime system orchestrator.

    This class manages the entire system lifecycle from initialization
    through runtime operation and shutdown.
    """

    def __init__(self, config_path: str = None):
        """
        Initialize Thalos Prime Core.

        Args:
            config_path: Path to configuration directory
        """
        logger.info("="*60)
        logger.info("THALOS PRIME CORE V1 - INITIALIZATION")
        logger.info("Copyright (c) 2026 Tony Ray Macier III")
        logger.info("="*60)

        self.config_path = config_path or "config"
        self.access_control = AccessControl()
        self.message_bus = MessageBus()
        self.system_monitor = SystemMonitor()

        # Core components
        self.sbi_engine = None
        self.matrix_codex = None
        self.input_pipeline = None
        self.reasoning_pipeline = None
        self.output_pipeline = None

        # GUI components
        self.window_manager = None
        self.io_ui = None

        # System state
        self.running = False

    def authenticate(self, passphrase: str = None) -> bool:
        """
        Authenticate system access.

        Args:
            passphrase: Master passphrase

        Returns:
            True if authentication successful
        """
        if passphrase is None:
            logger.info("Operating in development mode - authentication bypassed")
            return True

        if self.access_control.authenticate(passphrase):
            logger.info("✓ AUTHENTICATION SUCCESSFUL - Master access granted")
            return True
        else:
            logger.error("✗ AUTHENTICATION FAILED - Unauthorized access attempt")
            self.access_control.cerebral_hibernation()
            return False

    def initialize_core_systems(self):
        """Initialize core reasoning systems"""
        logger.info("Initializing core systems...")

        # Initialize SBI Engine
        logger.info("  - Initializing SBI Engine (Digital Thalamus)")
        self.sbi_engine = SBIEngine()

        # Initialize Matrix Codex
        logger.info("  - Initializing Matrix Codex (200M+ parameters)")
        codex_config = CodexConfig(
            num_layers=48,
            num_heads=32,
            hidden_dim=2048,
            ff_dim=8192
        )
        self.matrix_codex = MatrixCodex(codex_config)

        # Initialize pipelines
        logger.info("  - Initializing processing pipelines")
        self.input_pipeline = InputPipeline()
        self.reasoning_pipeline = ReasoningPipeline()
        self.output_pipeline = OutputPipeline()

        logger.info("✓ Core systems online")

    def initialize_gui(self):
        """Initialize graphical interface"""
        logger.info("Initializing GUI...")

        self.window_manager = WindowManager()

        # Create main blackboard window
        blackboard = self.window_manager.create_blackboard_window()

        # Add I/O interface
        self.io_ui = InputOutputUI(blackboard)

        # Add settings toolbar
        settings_toolbar = SettingsToolbar(self.window_manager.root)

        # Add status display
        status_tab = StatusTab(self.window_manager.root)

        logger.info("✓ GUI initialized")

    def setup_monitoring(self):
        """Setup system health monitoring"""
        logger.info("Setting up system monitoring...")

        # Register health checks
        self.system_monitor.register_monitor(
            "sbi_engine",
            lambda: self.sbi_engine is not None
        )

        self.system_monitor.register_monitor(
            "matrix_codex",
            lambda: self.matrix_codex is not None
        )

        self.system_monitor.start()
        logger.info("✓ System monitoring active")

    def process_input(self, user_input: str) -> str:
        """
        Process user input through the complete pipeline.

        Args:
            user_input: Raw user input text

        Returns:
            Generated response
        """
        logger.info(f"Processing input: {user_input[:50]}...")

        try:
            # Stage 1: Input processing
            normalized_input = self.input_pipeline.process(user_input)

            # Stage 2: SBI intent analysis
            intent_result = self.sbi_engine.process_input(user_input)

            # Stage 3: Reasoning (Bio-Digital synthesis)
            # Simulate biological state
            biological_state = self._get_biological_state()
            reasoning_result = self.reasoning_pipeline.reason(
                normalized_input,
                biological_state
            )

            # Stage 4: Output synthesis
            response = self.output_pipeline.synthesize(
                reasoning_result['output'],
                context=user_input
            )

            logger.info(f"✓ Response generated (confidence: {reasoning_result['confidence']:.3f})")

            return response

        except Exception as e:
            logger.error(f"Error processing input: {e}", exc_info=True)
            return f"Error: Unable to process input. {str(e)}"

    def _get_biological_state(self):
        """Get simulated biological state"""
        import numpy as np
        # In production, this would interface with real biological hardware
        return np.random.randn(64, 1000, 64) * 0.1

    def run(self, gui_mode: bool = True):
        """
        Run the Thalos Prime system.

        Args:
            gui_mode: Whether to run with GUI (True) or CLI (False)
        """
        self.running = True

        if gui_mode:
            logger.info("Starting in GUI mode...")
            self.window_manager.run()
        else:
            logger.info("Starting in CLI mode...")
            self._run_cli()

    def _run_cli(self):
        """Run in command-line interface mode"""
        print("\n" + "="*60)
        print("THALOS PRIME - Command Line Interface")
        print("Copyright (c) 2026 Tony Ray Macier III")
        print("="*60)
        print("\nType 'exit' to quit\n")

        while self.running:
            try:
                user_input = input("INPUT> ")

                if user_input.lower() in ['exit', 'quit']:
                    break

                if not user_input.strip():
                    continue

                response = self.process_input(user_input)
                print(f"\nOUTPUT> {response}\n")

            except KeyboardInterrupt:
                print("\n\nShutdown requested...")
                break
            except Exception as e:
                logger.error(f"Error in CLI loop: {e}", exc_info=True)

    def shutdown(self):
        """Gracefully shutdown all systems"""
        logger.info("Initiating graceful shutdown...")

        self.running = False

        # Stop monitoring
        if self.system_monitor:
            self.system_monitor.stop()

        logger.info("✓ Shutdown complete")
        logger.info("THALOS PRIME - SYSTEMS OFFLINE")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Thalos Prime Core V1 - Synthetic Biological Intelligence'
    )
    parser.add_argument(
        '--mode',
        choices=['gui', 'cli'],
        default='gui',
        help='Operation mode (default: gui)'
    )
    parser.add_argument(
        '--config',
        type=str,
        default='config',
        help='Path to configuration directory'
    )
    parser.add_argument(
        '--auth',
        type=str,
        help='Authentication passphrase (optional for dev mode)'
    )

    args = parser.parse_args()

    # Initialize Thalos Prime
    thalos = ThalosPrimeCore(config_path=args.config)

    # Authenticate
    if not thalos.authenticate(args.auth):
        logger.critical("Authentication failed - Exiting")
        sys.exit(1)

    try:
        # Initialize systems
        thalos.initialize_core_systems()

        if args.mode == 'gui':
            thalos.initialize_gui()

        thalos.setup_monitoring()

        # Run
        logger.info("✓ All systems operational - Launching Thalos Prime")
        thalos.run(gui_mode=(args.mode == 'gui'))

    except KeyboardInterrupt:
        logger.info("\nInterrupted by user")
    except Exception as e:
        logger.critical(f"Fatal error: {e}", exc_info=True)
    finally:
        thalos.shutdown()


if __name__ == "__main__":
    main()


# Sovereign verification
__author__ = "Tony Ray Macier III"
__copyright__ = "Copyright 2026, Thalos Prime Coding"
__license__ = "Proprietary - All Rights Reserved"
__version__ = "1.0.0-STABLE"
