from client import MobileTerminalCodingAssistantGatewayClient

def main():
    client = MobileTerminalCodingAssistantGatewayClient()
    res = client.get_agent_status("task-9021", "mobile_device_iOS_88")
    print(f"Task Status: {res['task_status']} ({res['progress_percentage']}%)")
    print(f"Summary: {res['live_terminal_summary']}")

if __name__ == "__main__":
    main()
