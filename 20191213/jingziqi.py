"""

井字棋

Version:1.0
Author:chaishuai

"""

import os

def print_board(board):
    os.system('cls')
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('------------')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('------------')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def move_in_chess(turn, board):
    tip = f'轮到{turn}下棋，请输入位置:'
    while True:
        position = input(tip)
        if position not in board.keys():
            tip = '不存在此位置，请重新选择位置:'
        elif board[position] != '   ':
            tip = '此位置已经落过子，请重新选择位置:'
        else:
            board[position] = f' {turn} '
            return board

def checkResult(turn, board):
    result_set = set()
    win_set = ({'TL', 'TM', 'TR'}, 
             {'ML', 'MM', 'MR'},
             {'BL', 'BM', 'BR'},
             {'TL', 'ML', 'BL'},
             {'TM', 'MM', 'BM'},
             {'TR', 'MR', 'BR'},
             {'BL', 'MM', 'BR'},
             {'TR', 'MM', 'BL'})
    for key in board:
        if board[key] == f' {turn} ':
            result_set.add(key)
    for set_x in win_set:
        if set_x - result_set == set():
            return True
    return False

def game(turn, board):
        print_board(board)
        board = move_in_chess(turn, board)
        print_board(board)
        if checkResult(turn, board) == True:
            need_next_game = input(f'{turn}获得了胜利，是否开始下一局(yes/no):')
            return need_next_game
        else:
            turn = 'o' if turn =='x' else 'x'
            game(turn, board)

def main():
    init_board = {'TL': '   ', 'TM': '   ', 'TR':'   ', 
                  'ML': '   ', 'MM': '   ', 'MR': '   ',
                  'BL': '   ', 'BM': '   ', 'BR': '   '}
    while True:
        board = init_board.copy()
        first_turn = 'x'
        need_next_game = game(first_turn, board)
        if need_next_game == 'no':
            break

if __name__ == '__main__':
    main()