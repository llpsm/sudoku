class Solve9x:
	def __init__(self, grid):
		self.grid = grid
		self.score = 0
		self.solve()

	def solve(self):
		fill_methods = [
			self.single_position,
			self.single_candidate,
		]
		cand_remove_methods = [
			self.candidate_lines
		]
		for method in fill_methods:
			while 1:
				filled = method()
				if not filled:
					break

		for method in cand_remove_methods:
			while 1:
				removed = method()
				if not removed: break
			self.single_position()
			self.single_candidate()


	def single_position(self):
		strat_score = 100
		filled = 0
		for x in range(9):
			for val in range(1, 10):
				cells = self.grid.rows_cands[x][val]
				if len(cells) == 1:
					cells[0].set_value(val)
					self.score += strat_score
					filled += 1

				cells = self.grid.cols_cands[x][val]
				if len(cells) == 1:
					cells[0].set_value(val)
					self.score += strat_score
					filled += 1

				cells = self.grid.boxs_cands[x][val]
				if len(cells) == 1:
					cells[0].set_value(val)
					self.score += strat_score
					filled += 1
		return filled > 0

	def single_candidate(self):
		strat_score = 100
		filled = 0
		for cell in self.grid.grid.values():
			if len(cell.candidates) == 1:
				cell.set_value(cell.candidates.pop())
				self.score += strat_score
				filled += 1
		return filled > 0

	def fill_after_remove(self, cell):
		strat_score = 100

		while 1:
			filled = 0
			if len(cell.candidates) == 1:
				cell.set_value(list(cell.candidates)[0])
				self.score += strat_score
				filled += 1

			for val in self.grid.values:
				rcells = self.grid.rows_cands[cell.r][val]
				if len(rcells) == 1:
					rcells[0].set_value(val)
					self.score += strat_score
					filled += 1

				ccells = self.grid.cols_cands[cell.c][val]
				if len(ccells) == 1:
					ccells[0].set_value(val)
					self.score += strat_score
					filled += 1

				bcells = self.grid.boxs_cands[cell.b][val]
				if len(bcells) == 1:
					bcells[0].set_value(val)
					self.score += strat_score
					filled += 1
			if not filled: break

	def candidate_lines(self):
		strat_score = 200
		removed = 0
		for b in range(9):
			for val, cells in self.grid.boxs_cands[b].items():
				rows = [cell.i//3 for cell in cells]
				if len(set(rows)) == 1:
					for cell in self.grid.rows_cands[cells[0].r][val]:
						if cell not in cells:
							cell.remove_candidate(val)
							self.score += strat_score
							removed += 1
							self.fill_after_remove(cell)

				cols = [cell.i%3 for cell in cells]
				if len(set(cols)) == 1:
					for cell in self.grid.cols_cands[cells[0].c][val]:
						if cell not in cells:
							cell.remove_candidate(val)
							self.score += strat_score
							removed += 1
							self.fill_after_remove(cell)
		return removed > 0