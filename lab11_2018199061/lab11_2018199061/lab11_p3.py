def copyFiles(f1, f2, f3):
    """ Copies files f1 and f2 onto file f3.
    If f1, f2 or f3 cannot be opened, -1 is returned.
    Otherwise, the copy operation is performed and 0 is returned.
    """

    try:
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

    except FileNotFoundError:
        return -1
