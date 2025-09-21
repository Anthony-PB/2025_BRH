// Create a new source
const createSource = async (sourceData: any) => {
    const response = await fetch('http://localhost:8000/api/sources/create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${localStorage.getItem('authToken')}`,
        },
        body: JSON.stringify(sourceData),
    });
    return response.json();
};

// Get all sources
const getSources = async () => {
    const response = await fetch('http://localhost:8000/api/sources/', {
        headers: {
            'Authorization': `Token ${localStorage.getItem('authToken')}`,
        },
    });
    return response.json();
};

// Get articles
const getArticles = async (sourceId?: string) => {
    const url = sourceId 
        ? `http://localhost:8000/api/articles/?source_id=${sourceId}`
        : 'http://localhost:8000/api/articles/';
    
    const response = await fetch(url, {
        headers: {
            'Authorization': `Token ${localStorage.getItem('authToken')}`,
        },
    });
    return response.json();
};

// Refresh articles from a source
const refreshSource = async (sourceId: string) => {
    const response = await fetch(`http://localhost:8000/api/refresh/${sourceId}/`, {
        method: 'POST',
        headers: {
            'Authorization': `Token ${localStorage.getItem('authToken')}`,
        },
    });
    return response.json();
};
