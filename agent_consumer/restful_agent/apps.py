import json
import os.path
import uuid

from django.apps import AppConfig


class AgentAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restful_agent'
    config = None

    def ready(self):
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')

        if not os.path.exists(config_path):
            # 如果文件不存在，创建默认配置
            random_secret = str(uuid.uuid4())
            default_config = {
                "secret": random_secret
            }
            print(f"第一次启动，保存访问密钥为: {random_secret}")
            with open(config_path, 'w') as f:
                json.dump(default_config, f, indent=4)

        # 加载配置文件
        with open(config_path, 'r') as f:
            self.config = json.load(f)

        # 打印确认配置已加载
        print("配置文件载入完成")
