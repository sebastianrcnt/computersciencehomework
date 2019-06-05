def copyFiles(f1, f2, f3):
    """
    Copies f1 and f2 onto f3.
    The function assumes that files f1 and f2 can be opened, and that
    no error occurs in writing file f3.

    Therefore, the function will always return 0.
    (Error handling with file I/O will be part of next week's lecture.)
    Parameters:
        f1, f2, f3 (string): name of file
    """

    # Open Files
    file1 = open(f1, 'r')
    file2 = open(f2, 'r')
    out = open(f3, 'w')

    # Write Text read from file2, file3
    out.write(file1.read())
    out.write(file2.read())

    # Close all Files
    file1.close()
    file2.close()
    out.close()

    return 0

copyFiles('in1.txt','in2.txt','in3.txt')