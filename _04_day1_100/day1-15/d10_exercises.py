def to_title_case(fname, lname):
    return (fname.title() + " " + lname.title())

def main():
    print(to_title_case("kermit","sibindi"))

if __name__ == "__main__":
    main()