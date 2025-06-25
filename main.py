from  TwitchSearcher import TwitchSearcher 
import argparse
import os

def do_event(filename):
    print(f"Start task : {filename}")

def notify_not_found(filename):
    print(f"File not Found : {filename}")

def parse_and_execute(file_path):
    ts = TwitchSearcher()  

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue
            cmd = parts[0]
            args = parts[1:]

            if cmd == "gotoWeb":
                ts.gotoWeb(*args)
            elif cmd == "search":
                ts.search(" ".join(args))
            elif cmd == "scroll":
                ts.scroll(args)
            elif cmd == "gotoChannel":
                ts.gotoRandomChannel()
            elif cmd == "gotoChannel":
                ts.gotoRandomChannel()
            elif cmd == "screenshot":
                ts.screenshot()
            elif cmd == "quit":
                ts.quit()
            else:
                print(f"⚠️ 不支援的指令：{cmd}")

if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description="逐一處理傳入的檔案")
    parser.add_argument("-s", "--source", nargs="+", help="一或多個指令檔 .txt")
    args = parser.parse_args()

    if args.source:
        for file in args.source:
            parse_and_execute(file)
    else:
        search = TwitchSearcher()
        link = "https://www.twitch.tv"
        keyword = "StarCraft II"
        search.gotoWeb(link)
        search.search(keyword)
        search.scroll(2)
        search.gotoRandomChannel()
        search.screenshot()
        search.quit()
