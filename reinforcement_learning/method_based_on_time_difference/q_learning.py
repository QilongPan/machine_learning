import random
from game import Game
'''
在更新St的动作值函数需要St+1的动作值函数，Sarsa用的是e-greedy方法，和选择St下的动作一样；
而Q-learning是用的greedy方法和选择St下动作不一样，因此称为off-policy
'''
class QLearning(object):

    def __init__(self):
        self.game = Game()
        self.iterator_number = 1000
        self.state_action_values = []
        for i in range(len(self.game.states)):
            state_action_value = []
            for j in range(len(self.game.actions)):
                state_action_value.append(0)
            self.state_action_values.append(state_action_value)
        self.alpha = 0.2

    #利用ε-greedy策略
    def epsilon_greedy(self,state,epsilon):
        best_action_index = 0
        best_value = self.state_action_values[state][0]
        for i in range(len(self.game.actions)):
            if best_value < self.state_action_values[state][i]:
                best_value = self.state_action_values[state][i]
                best_action_index = i

        probability = [0.0 for i in range(len(self.game.actions))]
        probability[best_action_index] += 1 - epsilon
        for i in range(len(self.game.actions)):
            probability[i] += epsilon / len(self.game.actions)

        random_number = random.random()
        sum_probability = 0.0
        for i in range(len(self.game.actions)):
            sum_probability += probability[i]
            if sum_probability >= random_number:
                return i
        return len(self.game.actions) - 1


    def greedy(self,state):
        best_action_index = 0
        best_value = self.state_action_values[state][best_action_index]
        for i in range(len(self.game.actions)):
            if best_value < self.state_action_values[state][i]:
                best_value = self.state_action_values[state][i]
                best_action_index = i
        return best_action_index
    
    def q_learning(self,epsilon):
        for i in range(self.iterator_number):
            state = self.game.states[random.randint(1,len(self.game.states) - 2)]
            action_index = random.randint(0,len(self.game.actions) - 1)
            move_number = 0
            while not self.game.is_end(state) and move_number < 50:
                next_state = self.game.do_action(state,self.game.actions[action_index])
                if next_state == 0 or next_state == 15:
                    reward = 1
                else:
                    reward = 0
                #寻找St+1的最大动作值采用的是greedy策略
                best_action_index = self.greedy(next_state)
                self.state_action_values[state][action_index] += self.alpha * (reward + self.game.gamma * self.state_action_values[next_state][best_action_index] - self.state_action_values[state][action_index])
                state = next_state
                #寻找St的下一动作采用的是ε-greedy策略
                #寻找St+1的最大动作值和寻找St的下一动作采用的策略不同，所以为异策略
                action_index = self.epsilon_greedy(next_state,epsilon)
                move_number += 1

if __name__ == '__main__':
    learn = QLearning()
    learn.q_learning(0.3)
    for state_action_value in learn.state_action_values:
        for value in state_action_value:
            print(round(value,1),end = "  ")
        print()