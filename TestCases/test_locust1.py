import locust

class MyUser(locust.HttpUser):
    """This function is aim to use locust+python to do performance testing. It requires starting Tomcat service."""
    # Create locust.HttpUser sub-class
    wait_time = locust.between(1, 2)
    # set 1~2 seconds interval between tasks.
    @locust.task
    def test_locust1(self):
        resp = self.client.get('http://192.168.1.158:8081/')
        # print("-----") # debug
        # print(resp) # debug
        # print("-----") # debug
        # print(resp.status_code) # debug
        # print("-----") # debug
        assert resp.status_code == 200

if __name__ == '__main__':
    myuser = MyUser()
    myuser.test_locust1()