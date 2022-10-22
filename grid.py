from cell import Cell

class Grid9x:
	values = {1, 2, 3, 4, 5, 6, 7, 8, 9}
	row_col_box_init_list = [[0,0,0,0,0,0,0,0,0] for i in range(9)]
	def __init__(self, grid):
		self._grid_dict = grid
		self.grid = {cn: Cell(self, cn, val) for cn, val in grid.items()}
		self.fill_init_lists()
		self.find_candidates()

	def fill_init_lists(self):
		self.rows = self._copy_list(self.row_col_box_init_list)
		self.cols = self._copy_list(self.row_col_box_init_list)
		self.boxs = self._copy_list(self.row_col_box_init_list)
		for cn, cell in self.grid.items():
			r, c, b, i = cell.rcbi
			self.rows[r][c] = self.cols[c][r] = self.boxs[b][i] = cell

	def find_candidates(self):
		self.rows_cands = self._new_cands_dict()
		self.cols_cands = self._new_cands_dict()
		self.boxs_cands = self._new_cands_dict()
		for cn, cell in self.grid.items():
			r, c, b, i = cell.rcbi
			if cell.value != 0:
				continue
			cell.candidates = self.values.difference(self.rows[r]).difference(self.cols[c]).difference(self.boxs[b])
			for val in cell.candidates:
				self.rows_cands[r][val].append(cell)
				self.cols_cands[c][val].append(cell)
				self.boxs_cands[b][val].append(cell)

	@property
	def is_solved(self):
		for cell in self.grid.values():
			if cell.value == 0:
				return False
		return True

	def print(self):
		g = self.grid
		grid_str = f'''
{g[ 0].value} {g[ 1].value} {g[ 2].value} | {g[ 3].value} {g[ 4].value} {g[ 5].value} | {g[ 6].value} {g[ 7].value} {g[ 8].value}
{g[ 9].value} {g[10].value} {g[11].value} | {g[12].value} {g[13].value} {g[14].value} | {g[15].value} {g[16].value} {g[17].value}
{g[18].value} {g[19].value} {g[20].value} | {g[21].value} {g[22].value} {g[23].value} | {g[24].value} {g[25].value} {g[26].value}
- - - | - - - | - - -
{g[27].value} {g[28].value} {g[29].value} | {g[30].value} {g[31].value} {g[32].value} | {g[33].value} {g[34].value} {g[35].value}
{g[36].value} {g[37].value} {g[38].value} | {g[39].value} {g[40].value} {g[41].value} | {g[42].value} {g[43].value} {g[44].value}
{g[45].value} {g[46].value} {g[47].value} | {g[48].value} {g[49].value} {g[50].value} | {g[51].value} {g[52].value} {g[53].value}
- - - | - - - | - - -
{g[54].value} {g[55].value} {g[56].value} | {g[57].value} {g[58].value} {g[59].value} | {g[60].value} {g[61].value} {g[62].value}
{g[63].value} {g[64].value} {g[65].value} | {g[66].value} {g[67].value} {g[68].value} | {g[69].value} {g[70].value} {g[71].value}
{g[72].value} {g[73].value} {g[74].value} | {g[75].value} {g[76].value} {g[77].value} | {g[78].value} {g[79].value} {g[80].value}
'''
		print(grid_str)

	def copy(self):
		return Grid9x(self._grid_dict)

	def _copy_list(self, old_list):
		new_list = []
		for sub_list in old_list:
			new_list.append(sub_list.copy())
		return new_list

	def _new_cands_dict(self):
		return {
			0: {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
			1: {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
			2: {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
			3: {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
			4: {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
			5: {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
			6: {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
			7: {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []},
			8: {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
		}
