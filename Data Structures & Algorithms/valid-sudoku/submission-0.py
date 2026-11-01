class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Проход по строкам
        for r in range(9):
            r_hashset = set()
            for s in range(9):
                val = board[r][s]

                if val == ".":
                    continue

                if val in r_hashset:
                    return False

                r_hashset.add(val)
                
        # Проход по столбцам
        for c in range(9):
            c_hashset = set()
            for r in range(9):
                val = board[r][c]

                if val == ".":
                    continue
                
                if val in c_hashset:
                    return False

                c_hashset.add(val)

        # Проход по квадратам

        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                sqr_hashset = set()
                for r in range(br, br + 3):
                    for c in range(bc, bc + 3):
                        val = board[r][c]
                        if val == ".":
                            continue
                        
                        if val in sqr_hashset:
                            return False
                        
                        sqr_hashset.add(val)
        return True


