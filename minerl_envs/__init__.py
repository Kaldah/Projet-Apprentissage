from gym.envs.registration import register


# Enregistrement des environnements

register(
    id='TestJump-v0',
    entry_point='minerl_envs.test_jump_env:CustomJumpEnv',
)

print("TestJump Environment registered as 'TestJump-v0'")


register(
    id='JumpAI-v0',
    entry_point='minerl_envs.jumpai_env:JumpAIEnv',
)

print("JumpAI Environment registered as 'AIJump-v0'")
