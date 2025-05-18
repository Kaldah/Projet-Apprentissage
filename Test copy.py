import minerl
import gym
import logging

def main():
    try:
        logging.basicConfig(level=logging.DEBUG)
        print("Launching environment...")
        env = gym.make('MineRLTreechop-v0')

        print("Resetting...")
        obs = env.reset()

        print("Success. Beginning loop.")
        done = False
        net_reward = 0

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
