#!/usr/bin/env python3
"""
SociaClip AI - Trend Scanner Module
Discovers trending YouTube videos and content across niches for clip extraction
"""

import json
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class TrendScanner:
    """Scans for trending content across different niches"""
    
    def __init__(self, brave_api_key: str = None):
        self.brave_api_key = brave_api_key or "BSAgcgZWW_ZL3hFjAxJ7vfug8SbHhJf"
        self.base_url = "https://api.search.brave.com/res/v1/web/search"
        
    def search_trending_videos(self, niche: str, days_back: int = 7) -> List[Dict]:
        """Search for trending videos in a specific niche"""
        
        # Construct search queries for different platforms and timeframes
        search_queries = [
            f"trending {niche} YouTube videos {datetime.now().strftime('%Y')}",
            f"viral {niche} content TikTok recent",
            f"popular {niche} videos this week",
            f"{niche} viral moments {datetime.now().strftime('%B')}",
            f"best {niche} clips going viral"
        ]
        
        all_results = []
        
        for query in search_queries:
            try:
                results = self._search_brave(query)
                all_results.extend(results)
            except Exception as e:
                print(f"Error searching for '{query}': {e}")
                
        return self._deduplicate_and_score(all_results, niche)
    
    def _search_brave(self, query: str) -> List[Dict]:
        """Execute search using Brave Search API"""
        
        headers = {
            "X-Subscription-Token": self.brave_api_key,
            "Accept": "application/json"
        }
        
        params = {
            "q": query,
            "count": 10,
            "freshness": "pw",  # Past week
            "text_decorations": False,
            "search_lang": "en"
        }
        
        response = requests.get(self.base_url, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        results = []
        
        if "web" in data and "results" in data["web"]:
            for result in data["web"]["results"]:
                results.append({
                    "title": result.get("title", ""),
                    "url": result.get("url", ""),
                    "description": result.get("description", ""),
                    "published": result.get("age", ""),
                    "source": "brave_search",
                    "search_query": query
                })
                
        return results
    
    def _deduplicate_and_score(self, results: List[Dict], niche: str) -> List[Dict]:
        """Remove duplicates and score content for viral potential"""
        
        # Simple deduplication by URL
        seen_urls = set()
        unique_results = []
        
        for result in results:
            url = result.get("url", "")
            if url and url not in seen_urls:
                seen_urls.add(url)
                unique_results.append(result)
        
        # Score each result for viral potential
        scored_results = []
        for result in unique_results:
            score = self._calculate_viral_score(result, niche)
            result["viral_score"] = score
            scored_results.append(result)
        
        # Sort by viral score (highest first)
        scored_results.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
        
        return scored_results[:20]  # Return top 20 results
    
    def _calculate_viral_score(self, result: Dict, niche: str) -> int:
        """Calculate viral potential score based on title, description, and keywords"""
        
        score = 0
        title = result.get("title", "").lower()
        description = result.get("description", "").lower()
        text = f"{title} {description}"
        
        # Viral keywords increase score
        viral_keywords = [
            "trending", "viral", "millions", "views", "breaking", "shocking",
            "amazing", "incredible", "unbelievable", "must see", "gone viral",
            "exploding", "massive", "huge", "crazy", "insane", "epic"
        ]
        
        for keyword in viral_keywords:
            if keyword in text:
                score += 10
        
        # Platform indicators
        if "youtube" in text:
            score += 15
        if "tiktok" in text:
            score += 12
        if "instagram" in text:
            score += 8
        
        # Recency indicators
        if any(word in text for word in ["today", "yesterday", "this week", "recent"]):
            score += 8
        
        # Number indicators suggest popularity
        if any(word in text for word in ["million", "billion", "thousand"]):
            score += 5
        
        # Niche relevance
        if niche.lower() in text:
            score += 20
        
        return score
    
    def get_top_niches(self) -> List[str]:
        """Return list of popular content niches for scanning"""
        return [
            "fitness", "business", "comedy", "gaming", "technology", 
            "food", "travel", "fashion", "music", "education",
            "motivation", "lifestyle", "sports", "news", "entertainment"
        ]

def main():
    """Test the trend scanner"""
    scanner = TrendScanner()
    
    # Test with fitness niche
    print("🔍 Scanning for trending fitness content...")
    results = scanner.search_trending_videos("fitness")
    
    print(f"Found {len(results)} trending videos:")
    for i, result in enumerate(results[:5]):
        print(f"{i+1}. {result['title']} (Score: {result['viral_score']})")
        print(f"   URL: {result['url']}")
        print(f"   Description: {result['description'][:100]}...")
        print()

if __name__ == "__main__":
    main()