#!/usr/bin/env python3
"""Nexa Notification - 智能通知"""
import json
from datetime import datetime

class NotificationManager:
    def __init__(self):
        self.notifications = []
        self.priority_levels = ["低", "中", "高", "紧急"]
    
    def add_notification(self, title, content, priority="中"):
        n = {
            "id": len(self.notifications) + 1,
            "title": title,
            "content": content,
            "priority": priority,
            "time": datetime.now().isoformat(),
            "read": False
        }
        self.notifications.append(n)
        return f"🔔 新通知: {title}"
    
    def get_unread(self):
        return [n for n in self.notifications if not n["read"]]
    
    def mark_read(self, notification_id):
        for n in self.notifications:
            if n["id"] == notification_id:
                n["read"] = True
                return "已标记为已读"
        return "通知不存在"

if __name__ == "__main__":
    nm = NotificationManager()
    print(nm.add_notification("好友消息", "Alice: 你好！", "高"))
    print(f"未读数量: {len(nm.get_unread())}")
