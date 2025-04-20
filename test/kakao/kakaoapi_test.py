import os

from dotenv import load_dotenv

from datakorea import kakaoapi


def test_kakaoapi():
    load_dotenv()
    REST_API_KEY = os.environ.get('API_KEY')
    REDIRECT_URI = os.environ.get('REDIRECT_URI')
    kakao_id = os.environ.get('KAKAO_ID')
    kakao_pw = os.environ.get('KAKAO_PW')

    print("rest api key : ", REST_API_KEY)
    print("redirect uri : ", REDIRECT_URI)
    print("kakao id : ", kakao_id)
    print("kakao pw : ", kakao_pw)

    m_kakao = kakaoapi(REST_API_KEY, REDIRECT_URI, kakao_id, kakao_pw)
    print("kakaoapi 객체 생성 완료")
    m_kakao.send_text_msg("kakao 메신저 테스트 메세지입니다!")
    print("send msg complete")

test_kakaoapi()