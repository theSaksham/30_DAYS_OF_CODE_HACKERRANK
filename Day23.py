

    def levelOrder(self,root):
        #Write your code here
        Q = []
        if (root.data is not None):
            Q.append(root)
        answer = ""
        while (Q):
            current = Q[0]
            answer = answer + str(current.data) + " "
            if current.left is not None:
                Q.append(current.left)
            if current.right is not None:
                Q.append(current.right)
            Q.pop(0)
        print(answer)


