def success(data=None, message: str = "success") -> dict:
    return {
        "success": True,
        "message": message,
        "data": data
    }


def fail(message: str = "failed", data=None) -> dict:
    return {
        "success": False,
        "message": message,
        "data": data
    }
