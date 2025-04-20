from datakorea import kakaoapi

REST_API_KEY = "REST API 키"
REDIRECT_URI = "REDIRECT URI"
kakao_id = "kakao 아이디"
kakao_pw = "kakao 비밀번호"

def test_kakaoapi():

    m_kakao = kakaoapi(REST_API_KEY, REDIRECT_URI, kakao_id, kakao_pw)
    print("kakaoapi 객체 생성 완료")
    m_kakao.send_text_msg("kakao 메신저 테스트 메세지입니다!")
    print("send msg complete")

test_kakaoapi()