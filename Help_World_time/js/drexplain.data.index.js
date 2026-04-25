DR_EXPLAIN.namespace( 'DR_EXPLAIN.data_index' );
DR_EXPLAIN.data_index = {

	// index
	DREX_NODE_KEYWORDS: [1,2],
	DREX_NODE_KEYWORDS_START: [0,0,0,2,2,2], //length:= drex.nodes_count,
	DREX_NODE_KEYWORDS_END: [0,0,2,2,2,2], //length:= drex.nodes_count,

	DREX_KEYWORD_NAMES: ["<НОВОЕ КЛЮЧЕВОЕ СЛОВО>","Имя","IP"],
	DREX_KEYWORD_CHILD_START: [1,3,3],
	DREX_KEYWORD_CHILD_END: [3,3,3]
	
};