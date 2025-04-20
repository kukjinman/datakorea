from datakorea.gerrit.gerritapi_manager import GerritAPIManager

if __name__ == "__main__":
    gerrit_url = "gerrit url"
    username = "사용자 id"
    password = "사용자 비밀번호"

    gerrit = GerritAPIManager(gerrit_url, username, password)

    result = gerrit.get_all_changes()
    print(result)
    # print(result[0]["change_id"])