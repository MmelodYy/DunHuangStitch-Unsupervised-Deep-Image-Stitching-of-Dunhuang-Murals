import torch

class solve_Size_DLT(object):
    def __init__(self):
        self.M1 = torch.tensor([
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0]], dtype=torch.float32).unsqueeze(0)
        self.M2 = torch.tensor([
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1]], dtype=torch.float32).unsqueeze(0)
        self.M3 = torch.tensor([
            [0],
            [1],
            [0],
            [1],
            [0],
            [1],
            [0],
            [1]], dtype=torch.float32).unsqueeze(0)
        self.M4 = torch.tensor([
            [-1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, -1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, -1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]], dtype=torch.float32).unsqueeze(0)
        self.M5 = torch.tensor([
            [0, -1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, -1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, -1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, -1],
            [0, 0, 0, 0, 0, 0, 0, 0]], dtype=torch.float32).unsqueeze(0)
        self.M6 = torch.tensor([
            [-1],
            [0],
            [-1],
            [0],
            [-1],
            [0],
            [-1],
            [0]], dtype=torch.float32).unsqueeze(0)
        self.M71 = torch.tensor([
            [0, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0]], dtype=torch.float32).unsqueeze(0)
        self.M72 = torch.tensor([
            [1, 0, 0, 0, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, -1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, -1, 0]], dtype=torch.float32).unsqueeze(0)
        self.M8 = torch.tensor([
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, -1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, -1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, -1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, -1]], dtype=torch.float32).unsqueeze(0)
        self.Mb = torch.tensor([
            [0, -1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, -1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, -1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, -1],
            [0, 0, 0, 0, 0, 0, 1, 0]], dtype=torch.float32).unsqueeze(0)

    def solve(self,pre_4pt_shift, size):
        bs, device, dtype = pre_4pt_shift.size(0), pre_4pt_shift.device, pre_4pt_shift.dtype
        pts_1_tile = torch.tile(size, [1, 4, 1])
        # print(pts_1_tile)
        tmp = torch.FloatTensor([0., 0., 1., 0., 0., 1., 1., 1.]).unsqueeze(0).unsqueeze(2).to(device)
        # print(pts_1_tile.shape,tmp.shape)
        pts_1_tile = pts_1_tile * tmp
        # print(pts_1_tile)
        # 4 points on the second image
        pred_pts_2_tile = pre_4pt_shift + pts_1_tile
        orig_pt4 = pred_pts_2_tile
        pred_pt4 = pts_1_tile
        # print(orig_pt4.shape,pred_pt4.shape)

        self.check_mat_device(device)
        # bs is dynamic
        A1 = torch.bmm(self.M1.expand(bs, -1, -1), orig_pt4)  # Column 1: [bs,8,8] x [bs,8,1] = [bs,8,1]
        A2 = torch.bmm(self.M2.expand(bs, -1, -1), orig_pt4)  # Column 2
        A3 = self.M3.expand(bs, -1, -1)  # Column 3: [bs, 8, 1]
        A4 = torch.bmm(self.M4.expand(bs, -1, -1), orig_pt4)  # Column 4
        A5 = torch.bmm(self.M5.expand(bs, -1, -1), orig_pt4)  # Column 5
        A6 = self.M6.expand(bs, -1, -1)  # Column 6
        A7 = torch.bmm(self.M71.expand(bs, -1, -1), pred_pt4) * torch.bmm(self.M72.expand(bs, -1, -1),
                                                                          orig_pt4)  # Column 7
        A8 = torch.bmm(self.M71.expand(bs, -1, -1), pred_pt4) * torch.bmm(self.M8.expand(bs, -1, -1),
                                                                          orig_pt4)  # Column 8

        A_mat = torch.cat((A1, A2, A3, A4, A5, A6, A7, A8), dim=-1)  # [bs,8,8]
        b_mat = torch.bmm(self.Mb.expand(bs, -1, -1), pred_pt4)  # [bs,8,1]
        # print(A_mat.shape,b_mat.shape)
        # Solve the Ax = b
        H_8el = torch.linalg.solve(A_mat.float(), b_mat.float()).type(dtype).squeeze(-1)  # [bs,8]

        h_ones = torch.ones((bs, 1)).to(device).type_as(H_8el)
        H_mat = torch.cat((H_8el, h_ones), dim=1).reshape(-1, 3, 3)  # [bs, 3, 3]

        return H_mat

    def check_mat_device(self, device):
        if self.M1.device != device:  # stupid
            self.M1 = self.M1.to(device)
            self.M2 = self.M2.to(device)
            self.M3 = self.M3.to(device)
            self.M4 = self.M4.to(device)
            self.M5 = self.M5.to(device)
            self.M6 = self.M6.to(device)
            self.M71 = self.M71.to(device)
            self.M72 = self.M72.to(device)
            self.M8 = self.M8.to(device)
            self.Mb = self.Mb.to(device)