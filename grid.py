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
		{g[ 0].value}\t{g[ 1].value}\t{g[ 2].value} | {g[ 3].value}\t{g[ 4].value}\t{g[ 5].value} | {g[ 6].value}\t{g[ 7].value}\t{g[ 8].value}
		{g[ 9].value}\t{g[10].value}\t{g[11].value} | {g[12].value}\t{g[13].value}\t{g[14].value} | {g[15].value}\t{g[16].value}\t{g[17].value}
		{g[18].value}\t{g[19].value}\t{g[20].value} | {g[21].value}\t{g[22].value}\t{g[23].value} | {g[24].value}\t{g[25].value}\t{g[26].value}
		-\t-\t-\t-\t-\t-\t-\t-\t-
		{g[27].value}\t{g[28].value}\t{g[29].value} | {g[30].value}\t{g[31].value}\t{g[32].value} | {g[33].value}\t{g[34].value}\t{g[35].value}
		{g[36].value}\t{g[37].value}\t{g[38].value} | {g[39].value}\t{g[40].value}\t{g[41].value} | {g[42].value}\t{g[43].value}\t{g[44].value}
		{g[45].value}\t{g[46].value}\t{g[47].value} | {g[48].value}\t{g[49].value}\t{g[50].value} | {g[51].value}\t{g[52].value}\t{g[53].value}
		-\t-\t-\t-\t-\t-\t-\t-\t-
		{g[54].value}\t{g[55].value}\t{g[56].value} | {g[57].value}\t{g[58].value}\t{g[59].value} | {g[60].value}\t{g[61].value}\t{g[62].value}
		{g[63].value}\t{g[64].value}\t{g[65].value} | {g[66].value}\t{g[67].value}\t{g[68].value} | {g[69].value}\t{g[70].value}\t{g[71].value}
		{g[72].value}\t{g[73].value}\t{g[74].value} | {g[75].value}\t{g[76].value}\t{g[77].value} | {g[78].value}\t{g[79].value}\t{g[80].value}
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
