import itertools

import pytest
from streamlit.testing.v1 import AppTest

APP = '../streamlit_app.py'
EXPLORE_OPTIONS = {
    'CSV': (['City', 'First_Name'], ['Age', 'Salary']),
    'JSON': (['department', 'address.city', 'address.state'], ['salary']),
    'Excel': (['Department'], ['Salary', 'Years_Of_Experience']),
}
AGGREGATIONS = ['sum', 'mean', 'median', 'min', 'max', 'count']


def run_app(source):
    at = AppTest.from_file(APP, default_timeout=60).run()
    at.sidebar.radio[0].set_value(source).run()
    assert not at.exception
    return at


@pytest.mark.parametrize('source', list(EXPLORE_OPTIONS))
def test_pipeline_and_dictionary_tabs_render(source):
    at = run_app(source)
    assert len(at.dataframe) >= 4
    assert len(at.json) == 1


@pytest.mark.parametrize('source', list(EXPLORE_OPTIONS))
def test_explore_tab_handles_every_combination(source):
    at = run_app(source)
    group_by_columns, value_columns = EXPLORE_OPTIONS[source]
    for group_by, value, aggregation in itertools.product(group_by_columns, value_columns, AGGREGATIONS):
        at.selectbox(key=f'{source}_group_by').select(group_by)
        at.selectbox(key=f'{source}_value').select(value)
        at.selectbox(key=f'{source}_aggregation').select(aggregation)
        at.run()
        assert not at.exception, (group_by, value, aggregation)
        assert at.code[-1].value == f"df.groupby('{group_by}')['{value}'].agg('{aggregation}')"
        assert 0 < len(at.dataframe[-1].value) <= 10
