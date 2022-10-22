from maps import cn_to_rcbi, rows, cols, boxs

class Cell:
	def __init__(self, grid, cn, value):
		self.grid = grid
		self.cn = cn
		self.value = value
		self.r, self.c, self.b, self.i = self.rcbi = cn_to_rcbi[cn]
		self.candidates = set()
		self.lists = []
		self.binded_cns = set(rows[self.r] + cols[self.c] + boxs[self.b])

	def set_value(self, value):
		self.value = value
		for cn in self.binded_cns:
			self.grid.grid[cn].remove_candidate(value)
		candidates = self.candidates.copy()
		for candidate in candidates:
			self.remove_candidate(candidate)

	def remove_candidate(self, candidate):
		if candidate in self.candidates:
			self.candidates.remove(candidate)
			self.grid.rows_cands[self.r][candidate].remove(self)
			self.grid.cols_cands[self.c][candidate].remove(self)
			self.grid.boxs_cands[self.b][candidate].remove(self)

	def __eq__(self, other):
		if isinstance(other, Cell):
			return self.cn == other.cn
		return self.value == other

	def __ne__(self, other):
		if isinstance(other, Cell):
			return self.cn != other.cn
		return self.value != other

	def __hash__(self):
		return self.value

	def __repr__(self):
		return f'({self.cn}, {self.value})'