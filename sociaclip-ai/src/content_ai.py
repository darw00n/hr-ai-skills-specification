#!/usr/bin/env python3
"""
SociaClip AI - Content Generation Module
AI-powered caption, hashtag, and hook generation for social media posts
"""

import json
import random
from typing import Dict, List, Optional
from datetime import datetime

class ContentAI:
    """AI-powered content generation for social media posts"""
    
    def __init__(self):
        self.platform_configs = {
            "instagram": {
                "max_caption_length": 2200,
                "hashtag_limit": 30,
                "optimal_hashtags": 5-10,
                "emoji_friendly": True
            },
            "tiktok": {
                "max_caption_length": 150,
                "hashtag_limit": 100,
                "optimal_hashtags": 3-5,
                "emoji_friendly": True
            },
            "youtube_shorts": {
                "max_caption_length": 1000,
                "hashtag_limit": 15,
                "optimal_hashtags": 5-8,
                "emoji_friendly": True
            },
            "twitter": {
                "max_caption_length": 280,
                "hashtag_limit": 2,
                "optimal_hashtags": 1-2,
                "emoji_friendly": True
            }
        }
    
    def generate_caption(self, video_data: Dict, platform: str, niche: str) -> str:
        """Generate engaging caption based on video data and platform"""
        
        title = video_data.get("title", "")
        description = video_data.get("description", "")
        viral_score = video_data.get("viral_score", 0)
        
        config = self.platform_configs.get(platform, self.platform_configs["instagram"])
        
        # Generate hook based on niche
        hook = self._generate_hook(niche, viral_score)
        
        # Generate main content
        main_content = self._generate_main_content(title, description, niche, platform)
        
        # Generate call to action
        cta = self._generate_cta(platform, niche)
        
        # Combine and optimize for platform
        caption = f"{hook}\n\n{main_content}\n\n{cta}"
        
        # Trim if too long for platform
        if len(caption) > config["max_caption_length"]:
            caption = caption[:config["max_caption_length"] - 3] + "..."
        
        return caption
    
    def generate_hashtags(self, video_data: Dict, platform: str, niche: str) -> List[str]:
        """Generate optimized hashtags for the platform and niche"""
        
        config = self.platform_configs.get(platform, self.platform_configs["instagram"])
        optimal_count = config["optimal_hashtags"]
        
        # Base hashtags for niche
        niche_hashtags = self._get_niche_hashtags(niche)
        
        # Trending hashtags (would be dynamically updated)
        trending_hashtags = self._get_trending_hashtags(platform)
        
        # Platform-specific hashtags
        platform_hashtags = self._get_platform_hashtags(platform)
        
        # Viral potential hashtags based on score
        viral_hashtags = self._get_viral_hashtags(video_data.get("viral_score", 0))
        
        # Combine and select best hashtags
        all_hashtags = niche_hashtags + trending_hashtags + platform_hashtags + viral_hashtags
        
        # Remove duplicates and select optimal count
        unique_hashtags = list(dict.fromkeys(all_hashtags))  # Preserves order
        
        if isinstance(optimal_count, tuple):
            count = random.randint(optimal_count[0], optimal_count[1])
        else:
            count = optimal_count
            
        return unique_hashtags[:count]
    
    def generate_posting_schedule(self, posts_per_day: int = 5) -> List[str]:
        """Generate optimal posting times for maximum engagement"""
        
        # Optimal posting times based on research
        peak_times = [
            "09:00",  # Morning commute
            "12:00",  # Lunch break
            "15:00",  # Afternoon break
            "18:00",  # After work
            "21:00"   # Evening entertainment
        ]
        
        if posts_per_day <= len(peak_times):
            return peak_times[:posts_per_day]
        else:
            # Distribute additional posts between peak times
            additional_times = ["10:30", "13:30", "16:30", "19:30", "22:30"]
            all_times = peak_times + additional_times
            return all_times[:posts_per_day]
    
    def _generate_hook(self, niche: str, viral_score: int) -> str:
        """Generate attention-grabbing hook based on niche and viral potential"""
        
        hooks_by_niche = {
            "fitness": [
                "🔥 This workout hack changes everything!",
                "💪 You won't believe this transformation!",
                "⚡ The secret trainers don't want you to know:",
                "🎯 This one move targets everything:",
                "🚀 Ready to level up your fitness game?"
            ],
            "business": [
                "💰 This business strategy is pure gold!",
                "📈 Want to 10x your income? Watch this:",
                "🧠 The millionaire mindset secret:",
                "⚡ This one pivot changed everything:",
                "🎯 The strategy billionaires use:"
            ],
            "comedy": [
                "😂 You're not ready for this!",
                "💀 This had me rolling!",
                "🤣 Wait for it... WAIT FOR IT!",
                "😭 Why is this so accurate?",
                "💯 The relatability is unreal!"
            ],
            "technology": [
                "🤖 AI just changed the game forever!",
                "📱 This tech hack will blow your mind:",
                "⚡ The future is happening right now:",
                "🔮 This innovation changes everything:",
                "🚀 Next-level technology alert:"
            ]
        }
        
        default_hooks = [
            "🔥 This is going viral for a reason!",
            "⚡ You need to see this:",
            "💯 This hits different:",
            "🎯 Pay attention to this:",
            "🚀 Game changer alert:"
        ]
        
        niche_hooks = hooks_by_niche.get(niche, default_hooks)
        
        # Add urgency for high viral score content
        if viral_score > 50:
            urgent_prefixes = ["🚨 VIRAL ALERT: ", "⚡ TRENDING NOW: ", "🔥 EVERYONE'S WATCHING: "]
            base_hook = random.choice(niche_hooks)
            return random.choice(urgent_prefixes) + base_hook.lower()
        
        return random.choice(niche_hooks)
    
    def _generate_main_content(self, title: str, description: str, niche: str, platform: str) -> str:
        """Generate main caption content based on video data"""
        
        # Extract key points from title and description
        content_templates = {
            "short": "{insight} This is exactly what {niche} content creators need to understand!",
            "medium": "Here's what caught my attention: {insight}\n\nThis perfectly shows why {niche} is evolving so fast right now.",
            "long": "Let me break this down for you:\n\n{insight}\n\nThis is the kind of {niche} content that's changing the game. The attention to detail is incredible!"
        }
        
        # Choose template based on platform
        if platform in ["twitter", "tiktok"]:
            template = content_templates["short"]
        elif platform == "instagram":
            template = content_templates["medium"]
        else:
            template = content_templates["long"]
        
        # Extract insight from title/description
        insight = self._extract_insight(title, description)
        
        return template.format(insight=insight, niche=niche)
    
    def _extract_insight(self, title: str, description: str) -> str:
        """Extract key insight from video title and description"""
        
        # Simple extraction - in production this would use AI/NLP
        text = f"{title} {description}".lower()
        
        insight_patterns = [
            "The technique that's taking over",
            "What everyone's talking about",
            "The trend that's everywhere",
            "The method that actually works",
            "What's changing the industry"
        ]
        
        return random.choice(insight_patterns)
    
    def _generate_cta(self, platform: str, niche: str) -> str:
        """Generate call-to-action based on platform"""
        
        ctas_by_platform = {
            "instagram": [
                "Double tap if you agree! 💫\nWhat's your take? Drop it in the comments! 👇",
                "Save this for later! 📌\nTag someone who needs to see this! 👀",
                "Hit that follow for more {niche} content! ✨"
            ],
            "tiktok": [
                "Follow for more! ✨",
                "What's your take? 👇", 
                "Share if this helped! 🔥"
            ],
            "youtube_shorts": [
                "Subscribe for more {niche} content! 🔔",
                "Like if this was helpful! 👍\nWhat should I cover next?",
                "Turn on notifications for more! ⚡"
            ],
            "twitter": [
                "Thoughts? 🤔",
                "RT if you agree! 🔄",
                "What's your experience? 👇"
            ]
        }
        
        platform_ctas = ctas_by_platform.get(platform, ctas_by_platform["instagram"])
        cta = random.choice(platform_ctas)
        
        return cta.format(niche=niche)
    
    def _get_niche_hashtags(self, niche: str) -> List[str]:
        """Get hashtags specific to the niche"""
        
        niche_hashtags = {
            "fitness": ["#fitness", "#workout", "#gym", "#health", "#fitnessmotivation", "#exercise"],
            "business": ["#business", "#entrepreneur", "#success", "#mindset", "#hustle", "#startup"],
            "comedy": ["#comedy", "#funny", "#humor", "#memes", "#lol", "#jokes"],
            "technology": ["#tech", "#technology", "#innovation", "#ai", "#future", "#digital"]
        }
        
        return niche_hashtags.get(niche, ["#viral", "#trending", "#content"])
    
    def _get_trending_hashtags(self, platform: str) -> List[str]:
        """Get currently trending hashtags (would be dynamically updated)"""
        
        # Mock trending hashtags - in production, these would be fetched from APIs
        return ["#viral", "#trending", "#fyp", "#explore", "#reels", "#shorts"]
    
    def _get_platform_hashtags(self, platform: str) -> List[str]:
        """Get platform-specific hashtags"""
        
        platform_hashtags = {
            "instagram": ["#reels", "#instagram", "#insta"],
            "tiktok": ["#fyp", "#foryou", "#tiktok"],
            "youtube_shorts": ["#shorts", "#youtube"],
            "twitter": ["#twitter", "#thread"]
        }
        
        return platform_hashtags.get(platform, [])
    
    def _get_viral_hashtags(self, viral_score: int) -> List[str]:
        """Get hashtags based on viral potential"""
        
        if viral_score > 70:
            return ["#viral", "#trending", "#exploding"]
        elif viral_score > 50:
            return ["#trending", "#popular", "#hot"]
        else:
            return ["#discover", "#new", "#fresh"]

def main():
    """Test the content AI system"""
    ai = ContentAI()
    
    # Mock video data
    video_data = {
        "title": "Amazing Fitness Transformation in 30 Days",
        "description": "This incredible workout routine changed everything for this person",
        "viral_score": 75
    }
    
    print("🤖 Testing Content AI Generation...")
    
    # Test caption generation for different platforms
    platforms = ["instagram", "tiktok", "youtube_shorts", "twitter"]
    
    for platform in platforms:
        print(f"\n📱 {platform.upper()}:")
        caption = ai.generate_caption(video_data, platform, "fitness")
        hashtags = ai.generate_hashtags(video_data, platform, "fitness")
        
        print(f"Caption: {caption}")
        print(f"Hashtags: {' '.join(hashtags)}")
        print("-" * 50)
    
    # Test posting schedule
    schedule = ai.generate_posting_schedule(5)
    print(f"\n⏰ Optimal posting schedule: {schedule}")

if __name__ == "__main__":
    main()