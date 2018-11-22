
from game import Game
import tensorflow as tf 
import random
class Dqn(Object):

    def __init__(self):
        self.game = Game()
        self.gamma = 0.9
        self.alpha = 0.3
        self.epsilon = 0.1
        self.iterator_number = 10000

    #利用ε-greedy策略
    def epsilon_greedy(self,state,epsilon):
        state_features = self.game.get_features(state)
        best_action_index = 0
        pre_state_action_value = sess.run(self.y,feed_dict={self.input_x:[state_features]})
        best_value = float("-inf")

        for i in range(len(self.game.actions)):
            if best_value < pre_state_action_value[0,i]:
                best_value = pre_state_action_value[0,i]
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

    def value_function(self,state,action):
        next_state = self.game.do_action(state,action)     
        features = self.game.get_features(next_state)
        return sess.run(self.y,feed_dict={self.input_x:np.array(features)})

    def dqn(self):
        self.input_x = tf.placeholder(tf.float32,shape = [None,16],name = 'input_name')
        self.input_y = tf.placeholder(tf.float32,shap = [None,1],name = "output_name")
        self.w = tf.Variable(tf.zeros([16,1]))
        self.b = tf.Variable(tf.zeros[1])
        self.y = tf.matmul(self.input_x,self.w) + b
        self.loss = tf.reduce_mean(tf.square(self.y - self.input_y))
        self.optimizer = tf.train.GradientDescentOptimizer(0.03)
        self.train = optimizer.minimize(self.loss)
        self.init = tf.global_variables_initializer()
        self.sess = tf.Session()
        self.sess.run(init)

        for i in range(self.iterator_number):
            state = random.choice(self.game.states)
            action_index = random.randint(0,len(self.game.actions) - 1)
            move_number = 0
            while not self.game.is_end(state) and move_number < 50:
                next_state = self.game.do_action(state,action_index)
                if next_state == 0 or next_state == 15:
                    reward = 1
                else:
                    reward = 0
                state_features = self.game.get_features(state)
                #取得最好的下一状态，采用greedy策略
                best_value = self.value_function(next_state,self.game.actions[0])
                for j in range(len(self.game.actions)):
                    value = self.value_function(state,self.game.actions[j])
                    if value > best_value:
                        best_value = value
                next_reward = reward + self.game.gamma * best_value
                sess.run(self.train,feed_dict = {self.input_x:[np.array(state_features)],self.input_y:next_reward})
                state = next_state
                #走步策略采用ε-greedy策略
                action_index = self.epsilon_greedy(next_state,epsilon)
                move_number += 1                

if __name__ == "__main__":
    pass








