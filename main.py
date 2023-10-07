from AutoBugger import AutoBugger


def main(name):
    auto_bugger = AutoBugger()
    print("Start AutoBugger")
    auto_bugger.Start()

    auto_bugger.Stop()
    print("AutoBugger complete")


if __name__ == '__main__':
    main('PyCharm')
