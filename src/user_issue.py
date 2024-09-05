from typing import Optional
class UserIssue:
    def __init__(self):
        self.issue_type: Optional[str] = None
        self.details: Optional[str] = None

    def set_issue_type(self, issue_type: str):
        if not isinstance(issue_type, str):
            raise ValueError("issue_type must be a string")
        self.issue_type = issue_type
    def set_details(self, details: str):
        if not isinstance(details, str):
            raise ValueError("details must be a string")
        self.details = details


functions = [
    {
        "name": "handle_user_issue",
        "description": "Handle an issue detected in user input",
        "parameters": {
            "type": "object",
            "properties": {
                "issue_type": {
                    "type": "string",
                    "description": "The type of issue detected"
                },
                "details": {
                    "type": "string",
                    "description": "Detailed description/the reason of the issue"
                }
            },
            "required": ["issue_type", "details"]
        }
    }
]

def handle_user_issue(user_issue: UserIssue) -> None:
    """
    Might be useful later for answer processing
    """
    print(f"Handling issue: {user_issue.issue_type} with details: {user_issue.details}")