def solution(board, moves):
    answer = 0 #답
    temp=[] #바구니에담긴인형들
    temp_idx=0 #바구니에 담긴인형들의 index
    for i in range(len(moves)): 
        for j in range(len(board)):
            if board[j][moves[i]-1]>0:
                temp.insert(temp_idx,board[j][moves[i]-1])
                temp_idx+=1
                board[j][moves[i]-1]=0
                break
        if len(temp)>1 and temp[temp_idx-1]!=0:
            if temp[temp_idx-2]==temp[temp_idx-1]:
                temp[temp_idx-2]=0
                temp[temp_idx-1]=0
                answer+=2
                temp_idx-=2    
    return answer
