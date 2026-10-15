with open('demo.txt', 'r') as rf:
    with open('demo_copy.txt', 'w') as wf:
        # chunk_size = 10
        # rf_chunk = rf.read(chunk_size)
        # while len(rf_chunk) > 0:
        #     wf.write(rf_chunk)
        #     rf_chunk = rf.read(chunk_size)
        for line in rf:
            wf.write(line)


    
    # size_to_read = 10
    # f_comtent = f.read(size_to_read)
    # print(f_comtent, end='')

    # f.seek(0)

    # f_comtent = f.read(size_to_read)
    # print(f_comtent, end='')
    # print(f.tell())
    # f_comtent = f.readline()
    # print(f_comtent, end='')

    # f_comtent = f.readline()
    # print(f_comtent, end='')
    
    # for line in f:
    #     print(line, end='')



