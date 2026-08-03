class MobileTerminalCodingAssistantGatewayClient:
    def get_agent_status(self, active_agent_task_id: str, mobile_device_id: str) -> dict:
        return {
            "task_status": "EXECUTING_REFACTORING",
            "progress_percentage": 78.5,
            "live_terminal_summary": f"Task {active_agent_task_id}: Successfully compiled 14 files, running unit test suite."
        }
