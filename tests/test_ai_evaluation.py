def mock_llm_response(prompt):
    # Simulates an AI Agent response
    return {"prompt": prompt, "response": "Automic provides cloud-native registry services.", "grounded": True}

def test_ai_response_groundedness():
    prompt = "What services does Automic offer?"
    result = mock_llm_response(prompt)
    
    # Assert response contains required domain key terms
    expected_keywords = ["cloud-native", "registry"]
    for keyword in expected_keywords:
        assert keyword in result["response"], f"Missing expected grounded keyword: {keyword}"
    
    assert result["grounded"] is True