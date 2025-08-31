def rut_gon_path(path):
    phan_tu = path.split("/")
    ngan_xep = []
    for p in phan_tu:
        if p == "" or p == ".":
            continue
        elif p == "..":
            if ngan_xep:
                ngan_xep.pop()
        else:
# test-------------------------------------------------------------
