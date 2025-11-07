import sys
import time

sys.path.insert(0, "../src")

from unitree.unitree_sdk2py.core.channel import (
    ChannelFactoryInitialize,
    ChannelSubscriber,
)
from unitree.unitree_sdk2py.idl.unitree_go.msg.dds_ import SportModeState_


class Custom:
    def __init__(self):
        self.low_state = None

    def Init(self):
        self.sportstate_subscriber = ChannelSubscriber(
            "rt/sportmodestate", SportModeState_
        )
        self.sportstate_subscriber.Init(self.SportStateMessageHandler, 10)

    ddef SportStateMessageHandler(self, msg: SportModeState_):
    """Handle incoming SportModeState messages."""
    self.low_state = msg
    print(f"[SportState] Error Code: {msg.error_code}, Mode: {msg.mode}")


if __name__ == "__main__":

    if len(sys.argv) > 1:
        ChannelFactoryInitialize(0, sys.argv[1])
    else:
        ChannelFactoryInitialize(0)

    custom = Custom()
    custom.Init()

    while True:
        time.sleep(1)
