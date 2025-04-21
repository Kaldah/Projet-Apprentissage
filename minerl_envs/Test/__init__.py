from gym.envs.registration import register

register(
    id='CustomJump-v0',
    entry_point='minerl_envs.Test.custom_jump_env:CustomJumpEnv',
)
