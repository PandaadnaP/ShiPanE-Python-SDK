import shipane_sdk


def init(context):
    context.s1 = "000001.XSHE"

def before_trading(context):
    # 创建 RiceQuantStrategyManagerFactory 对象
    # 参数为 shipane_sdk_config_template.yaml 中配置的 manager id
    context.__manager = shipane_sdk.RiceQuantStrategyManagerFactory(context).create('manager-1')

def handle_bar(context, bar_dict):
    try:
        order_target_value(context.s1, 0)
        order_target_value(context.s1, 500)
    finally:
        # 放在 finally 块中，以防原有代码抛出异常或者 return
        # 在函数结尾处加入以下语句，用来将模拟盘同步至实盘
        g.__manager.work()
