from trendradar.core.loader import load_config
config = load_config()
print("DINGTALK_WEBHOOK_URL:", config.get("DINGTALK_WEBHOOK_URL"))
print("DINGTALK_SECRET:", config.get("DINGTALK_SECRET"))