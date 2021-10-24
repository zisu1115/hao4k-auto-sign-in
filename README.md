# Hao4K 网站自动签到脚本

利用Github Actions功能实现Hao4K.cn网站自动签到，并将结果推送至Telegram。  

## 脚本功能
- 每日上午7点定时执行签到功能。
- 支持签到结果消息推送至你的Telegram Bot。

## 使用方法
- Fork本仓库；
- 由于Hao4K个人账户信息需要保密，所以将其配置到仓库的`setting/secrets`下：
    - 在你Fork的仓库名下，单击`Settings`（设置）；
    - 在左侧栏单击`Secrets`（密码）；
    - 单击`New repository secret`（新密码）；
    - 逐个键入密码的名称`Name`和密码对应的值，分别是：
        - `HAO4K_USERNAME` 网站的用户名
        - `HAO4K_PASSWORD` 网站的密码
        - `TG_BOT_TOKEN` Telgram Bot的TOKEN
        - `TG_CHAT_ID` Telegram的Chat ID
    - 如何获取Telegram机器人的TOKEN和你的Chat ID下面会讲，也可以自行Google；
    - 修改任务执行时间，在[.github/workflows/ci.yml](https://github.com/bychen009/hao4k-auto-sign-in/blob/master/.github/workflows/ci.yml) line 13,找到`cron: '0 23 * * *'`表达式，修改其中的23为你想要的时间，注意这里是GMT时间，+8才是北京时间,[参考文档](https://docs.github.com/cn/actions/reference/events-that-trigger-workflows#scheduled-events)。

## 注册Telegram机器人并获取TOKEN
注册过程比较简单，在Telegram中与“机器人之父”聊天，即`@BotFather`这个账号。
- 打开与`@BotFather`的会话
- 点击/start
- 发送/newbot
- 发送你要注册的Bot昵称
- 发送Bot的ID（不可修改）
- 得到Bot的token，用于标识这个Bot
- 打开与你Bot的会话，随意发送一个消息，比如`Hello`

## 获取Chat ID  
- 打开与`@getuseridbot`的会话
- 点击/start
- 得到你的Chat ID

## 自动同步上游代码
安装Github App [Pull](https://github.com/apps/pull)，将fork后的项目添加到Repository access列表中即可实现自动同步上游代码。
