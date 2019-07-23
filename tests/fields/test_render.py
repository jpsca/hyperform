import proper_form.fields as f
from proper_form.fields.render import get_html_attrs


def test_html_attrs():
    attrs = {
        "id": "text1",
        "className": "myclass",
        "data_id": 1,
        "checked": True,
        "ignore": False,
    }
    assert get_html_attrs(attrs) == \
        'class="myclass" data-id="1" id="text1" checked'


def test_html_attrs_empty():
    assert get_html_attrs() == ""


def test_html_attrs_bad():
    assert get_html_attrs({"myattr": "a'b\"><script>bad();</script>"}) == \
        'myattr="a\'b&quot;&gt;&lt;script&gt;bad();&lt;/script&gt;"'


def test_render_attrs():
    field = f.Text()
    attrs = {
        "id": "text1",
        "className": "myclass",
        "data_id": 1,
        "checked": True,
        "ignore": False,
    }
    assert str(field.render_attrs(**attrs)) == \
        'class="myclass" data-id="1" id="text1" checked'


def test_render_attrs_empty():
    field = f.Text()
    assert str(field.render_attrs()) == ""


def test_render_attrs_bad():
    field = f.Text()
    assert str(field.render_attrs(myattr="a'b\"><script>bad();</script>")) == \
        'myattr="a\'b&quot;&gt;&lt;script&gt;bad();&lt;/script&gt;"'


def test_object_value():
    field = f.Text(prepare=lambda x: [str(x * 2)])
    field.object_value = 2
    assert field.values == ["4"]
    assert field.value == "4"


def test_input_values():
    field = f.Text()
    field.input_values = ["hello"]
    assert field.values == ["hello"]
    assert field.value == "hello"


def test_input_value_over_object_value():
    field = f.Text()
    field.input_values = ["foo"]
    field.object_value = "bar"
    assert field.values == ["foo"]
    assert field.value == "foo"


def test_auto_id():
    assert f.Text(name="name").auto_id == "form_name"
    assert f.Text(name="password").auto_id == "form_password"
    field = f.Text(name="email")
    field.prefix = "userForm"
    assert field.auto_id == "userForm_email"
