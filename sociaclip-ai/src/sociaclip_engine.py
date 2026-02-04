#!/usr/bin/env python3
"""
SociaClip AI - Main Engine
Orchestrates the entire content discovery, generation, and posting workflow
"""

import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from trend_scanner import TrendScanner
from content_ai import ContentAI

class SociaClipEngine:
    """Main engine for SociaClip AI automation"""
    
    def __init__(self, config: Dict = None):
        self.config = config or self._get_default_config()
        self.trend_scanner = TrendScanner()
        self.content_ai = ContentAI()
        self.daily_posts = []
        
    def _get_default_config(self) -> Dict:
        """Get default configuration for the engine"""
        return {
            "posts_per_day": 5,
            "target_niches": ["fitness", "business", "technology", "comedy"],
            "platforms": ["instagram", "tiktok", "youtube_shorts", "twitter"],
            "posting_schedule": ["09:00", "12:00", "15:00", "18:00", "21:00"],
            "min_viral_score": 30,
            "content_freshness_hours": 24
        }
    
    def run_daily_workflow(self, niche: str = None) -> Dict:
        """Execute the complete daily content workflow"""
        
        workflow_start = datetime.now()
        results = {
            "status": "running",
            "start_time": workflow_start.isoformat(),
            "niche": niche,
            "posts_generated": 0,
            "posts_scheduled": 0,
            "errors": []
        }
        
        try:
            # Step 1: Discover trending content
            print(f"🔍 Step 1: Discovering trending content for {niche or 'all niches'}...")
            trending_videos = self._discover_content(niche)
            print(f"   Found {len(trending_videos)} trending videos")
            
            # Step 2: Filter and select best content
            print("🎯 Step 2: Selecting best content for posts...")
            selected_content = self._select_content(trending_videos)
            print(f"   Selected {len(selected_content)} pieces of content")
            
            # Step 3: Generate AI content for each platform
            print("🤖 Step 3: Generating AI captions and hashtags...")
            generated_posts = self._generate_content(selected_content, niche or "mixed")
            print(f"   Generated {len(generated_posts)} social media posts")
            results["posts_generated"] = len(generated_posts)
            
            # Step 4: Schedule posts
            print("⏰ Step 4: Scheduling posts across platforms...")
            scheduled_posts = self._schedule_posts(generated_posts)
            print(f"   Scheduled {len(scheduled_posts)} posts")
            results["posts_scheduled"] = len(scheduled_posts)
            
            # Step 5: Save for analytics
            print("📊 Step 5: Saving posts for performance tracking...")
            self._save_posts_for_analytics(scheduled_posts)
            
            results["status"] = "completed"
            results["end_time"] = datetime.now().isoformat()
            results["duration_minutes"] = (datetime.now() - workflow_start).seconds / 60
            results["daily_posts"] = scheduled_posts
            
            print("✅ Daily workflow completed successfully!")
            return results
            
        except Exception as e:
            results["status"] = "error"
            results["error"] = str(e)
            results["errors"].append(str(e))
            print(f"❌ Error in workflow: {e}")
            return results
    
    def _discover_content(self, niche: str = None) -> List[Dict]:
        """Discover trending content across niches"""
        
        all_videos = []
        niches_to_scan = [niche] if niche else self.config["target_niches"]
        
        for scan_niche in niches_to_scan:
            try:
                videos = self.trend_scanner.search_trending_videos(scan_niche)
                for video in videos:
                    video["source_niche"] = scan_niche
                all_videos.extend(videos)
                
                # Rate limiting protection
                time.sleep(1)
                
            except Exception as e:
                print(f"   Warning: Error scanning {scan_niche}: {e}")
                continue
        
        return all_videos
    
    def _select_content(self, trending_videos: List[Dict]) -> List[Dict]:
        """Select the best content for posting"""
        
        # Filter by minimum viral score
        min_score = self.config["min_viral_score"]
        high_quality_videos = [v for v in trending_videos if v.get("viral_score", 0) >= min_score]
        
        # Sort by viral score
        high_quality_videos.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
        
        # Select top videos for posts per day
        posts_needed = self.config["posts_per_day"]
        selected = high_quality_videos[:posts_needed * 2]  # Get extra for variety
        
        return selected
    
    def _generate_content(self, selected_videos: List[Dict], niche: str) -> List[Dict]:
        """Generate AI content for social media posts"""
        
        generated_posts = []
        platforms = self.config["platforms"]
        posts_per_platform = max(1, self.config["posts_per_day"] // len(platforms))
        
        video_index = 0
        for platform in platforms:
            for i in range(posts_per_platform):
                if video_index >= len(selected_videos):
                    break
                    
                video = selected_videos[video_index]
                
                try:
                    # Generate caption and hashtags
                    caption = self.content_ai.generate_caption(video, platform, niche)
                    hashtags = self.content_ai.generate_hashtags(video, platform, niche)
                    
                    post = {
                        "id": f"{platform}_{datetime.now().strftime('%Y%m%d')}_{i}",
                        "platform": platform,
                        "video_source": video,
                        "caption": caption,
                        "hashtags": hashtags,
                        "full_post": f"{caption}\n\n{' '.join(hashtags)}",
                        "niche": niche,
                        "created_at": datetime.now().isoformat(),
                        "viral_score": video.get("viral_score", 0)
                    }
                    
                    generated_posts.append(post)
                    video_index += 1
                    
                except Exception as e:
                    print(f"   Warning: Error generating content for {platform}: {e}")
                    video_index += 1
                    continue
        
        return generated_posts
    
    def _schedule_posts(self, generated_posts: List[Dict]) -> List[Dict]:
        """Schedule posts for optimal engagement times"""
        
        schedule = self.config["posting_schedule"]
        scheduled_posts = []
        
        for i, post in enumerate(generated_posts):
            if i >= len(schedule):
                break
                
            posting_time = schedule[i]
            post["scheduled_time"] = posting_time
            post["scheduled_date"] = datetime.now().strftime("%Y-%m-%d")
            post["status"] = "scheduled"
            
            scheduled_posts.append(post)
        
        return scheduled_posts
    
    def _save_posts_for_analytics(self, posts: List[Dict]):
        """Save posts for performance tracking"""
        
        filename = f"posts_{datetime.now().strftime('%Y-%m-%d')}.json"
        filepath = f"data/scheduled_posts/{filename}"
        
        # Create directory if needed
        import os
        os.makedirs("data/scheduled_posts", exist_ok=True)
        
        with open(filepath, 'w') as f:
            json.dump({
                "generated_at": datetime.now().isoformat(),
                "total_posts": len(posts),
                "platforms": list(set(p["platform"] for p in posts)),
                "posts": posts
            }, f, indent=2)
        
        print(f"   Saved {len(posts)} posts to {filepath}")
    
    def get_performance_summary(self, days: int = 7) -> Dict:
        """Get performance summary for recent posts"""
        
        # Mock performance data - in production this would query actual analytics
        return {
            "period": f"Last {days} days",
            "total_posts": self.config["posts_per_day"] * days,
            "total_engagement": 15420,
            "avg_engagement_per_post": 220,
            "top_performing_platform": "instagram",
            "top_performing_niche": "fitness",
            "engagement_trend": "+12%",
            "follower_growth": "+8%"
        }
    
    def optimize_strategy(self) -> Dict:
        """Analyze performance and suggest optimizations"""
        
        # Mock optimization suggestions - in production this would use ML
        return {
            "recommendations": [
                "Increase fitness content by 20% - highest engagement rate",
                "Post more often on Instagram during 6-8 PM window",
                "Add more trending hashtags to TikTok posts",
                "Use shorter captions on Twitter for better engagement"
            ],
            "optimal_posting_times": {
                "instagram": ["18:00", "21:00"],
                "tiktok": ["19:00", "22:00"], 
                "youtube_shorts": ["20:00", "15:00"],
                "twitter": ["12:00", "17:00"]
            },
            "content_mix": {
                "fitness": 30,
                "business": 25,
                "technology": 25,
                "comedy": 20
            }
        }

def main():
    """Test the main engine"""
    print("🚀 Testing SociaClip AI Engine...")
    
    engine = SociaClipEngine()
    
    # Run workflow for fitness niche
    results = engine.run_daily_workflow("fitness")
    
    print("\n📊 Workflow Results:")
    print(json.dumps(results, indent=2, default=str))
    
    # Get performance summary
    print("\n📈 Performance Summary:")
    performance = engine.get_performance_summary()
    print(json.dumps(performance, indent=2))
    
    # Get optimization suggestions
    print("\n🎯 Optimization Recommendations:")
    optimizations = engine.optimize_strategy()
    print(json.dumps(optimizations, indent=2))

if __name__ == "__main__":
    main()