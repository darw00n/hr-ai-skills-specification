#!/usr/bin/env python3
"""
SociaClip AI - Enhanced Content Generation Module
Advanced AI content generation with improved templates, hooks, and platform optimization
"""

import json
import random
import re
from typing import Dict, List, Optional, Tuple
from datetime import datetime

class EnhancedContentAI:
    """Enhanced AI-powered content generation with advanced templates and optimization"""
    
    def __init__(self):
        self.platform_configs = {
            "instagram": {
                "max_caption_length": 2200,
                "hashtag_limit": 30,
                "optimal_hashtags": (8, 12),
                "emoji_friendly": True,
                "supports_stories": True,
                "supports_reels": True,
                "peak_times": ["11:00", "14:00", "17:00", "20:00"]
            },
            "tiktok": {
                "max_caption_length": 150,
                "hashtag_limit": 100,
                "optimal_hashtags": (3, 5),
                "emoji_friendly": True,
                "supports_effects": True,
                "supports_duets": True,
                "peak_times": ["18:00", "19:00", "20:00", "21:00"]
            },
            "youtube_shorts": {
                "max_caption_length": 1000,
                "hashtag_limit": 15,
                "optimal_hashtags": (5, 8),
                "emoji_friendly": True,
                "supports_end_screens": True,
                "peak_times": ["14:00", "16:00", "18:00", "20:00"]
            },
            "twitter": {
                "max_caption_length": 280,
                "hashtag_limit": 2,
                "optimal_hashtags": (1, 2),
                "emoji_friendly": True,
                "supports_threads": True,
                "peak_times": ["09:00", "12:00", "15:00", "18:00"]
            }
        }
        
        self.viral_hooks_database = self._build_viral_hooks_database()
        self.engagement_templates = self._build_engagement_templates()
        self.niche_expertise = self._build_niche_expertise()
    
    def generate_advanced_post(self, video_data: Dict, platform: str, niche: str, 
                             engagement_style: str = "viral") -> Dict:
        """Generate advanced post with multiple optimization layers"""
        
        config = self.platform_configs.get(platform, self.platform_configs["instagram"])
        viral_score = video_data.get("viral_score", 0)
        
        # Select optimal content strategy
        content_strategy = self._select_content_strategy(viral_score, platform, niche)
        
        # Generate multiple hook options
        hook_options = self._generate_multiple_hooks(niche, viral_score, platform, 3)
        best_hook = self._select_best_hook(hook_options, engagement_style)
        
        # Generate sophisticated main content
        main_content = self._generate_advanced_content(
            video_data, platform, niche, content_strategy
        )
        
        # Generate smart call-to-action
        cta = self._generate_smart_cta(platform, niche, engagement_style, viral_score)
        
        # Generate optimized hashtags with trending analysis
        hashtags = self._generate_optimized_hashtags(
            video_data, platform, niche, viral_score
        )
        
        # Combine and optimize
        full_caption = self._combine_and_optimize(
            best_hook, main_content, cta, config["max_caption_length"]
        )
        
        # Generate posting recommendations
        posting_rec = self._generate_posting_recommendations(platform, viral_score)
        
        return {
            "platform": platform,
            "caption": full_caption,
            "hashtags": hashtags,
            "full_post": f"{full_caption}\n\n{' '.join(hashtags)}",
            "content_strategy": content_strategy,
            "engagement_style": engagement_style,
            "hook_options": hook_options,
            "selected_hook": best_hook,
            "posting_recommendations": posting_rec,
            "viral_score": viral_score,
            "optimization_score": self._calculate_optimization_score(
                full_caption, hashtags, platform, viral_score
            ),
            "created_at": datetime.now().isoformat()
        }
    
    def _build_viral_hooks_database(self) -> Dict:
        """Build comprehensive database of viral hooks by niche and intensity"""
        
        return {
            "fitness": {
                "low_intensity": [
                    "Here's a simple fitness tip:",
                    "Small change, big results:",
                    "This workout tip helped me:",
                ],
                "medium_intensity": [
                    "🔥 This fitness hack changed my routine:",
                    "💪 The workout secret that actually works:",
                    "⚡ This one move targets everything:",
                ],
                "high_intensity": [
                    "🚨 FITNESS TRAINERS HATE THIS TRICK:",
                    "💀 This workout DESTROYED me (in the best way):",
                    "🔥 GOING VIRAL: The 30-second move that changed everything:",
                    "⚡ MILLION VIEWS: This technique is INSANE:",
                ]
            },
            "business": {
                "low_intensity": [
                    "Business insight for today:",
                    "Here's what I learned:",
                    "Quick business tip:",
                ],
                "medium_intensity": [
                    "💰 The business strategy that's working:",
                    "📈 How I 10x'd my productivity:",
                    "🧠 The mindset shift that changed everything:",
                ],
                "high_intensity": [
                    "🚨 MILLIONAIRES DON'T WANT YOU TO KNOW THIS:",
                    "💸 I made $100k with this ONE strategy:",
                    "🔥 VIRAL BUSINESS HACK: How I automated everything:",
                    "⚡ THE SECRET: Why 99% of entrepreneurs fail:",
                ]
            },
            "technology": {
                "low_intensity": [
                    "Cool tech discovery:",
                    "This app changed my workflow:",
                    "Tech tip of the day:",
                ],
                "medium_intensity": [
                    "🤖 This AI tool is incredible:",
                    "📱 The app that saves me 5 hours/week:",
                    "⚡ Technology hack that's a game-changer:",
                ],
                "high_intensity": [
                    "🚨 AI JUST BROKE THE INTERNET:",
                    "🤯 THIS TECHNOLOGY WILL CHANGE EVERYTHING:",
                    "🔥 VIRAL TECH: The future is happening NOW:",
                    "⚡ MILLIONS WATCHING: This AI can do WHAT?!",
                ]
            },
            "comedy": {
                "low_intensity": [
                    "This made me chuckle:",
                    "Relatable moment:",
                    "Daily dose of humor:",
                ],
                "medium_intensity": [
                    "😂 This is too accurate:",
                    "💀 Why is this so true?",
                    "🤣 The relatability is unreal:",
                ],
                "high_intensity": [
                    "😭 I'M SCREAMING - this is TOO REAL:",
                    "💀 DEATH BY LAUGHTER - I can't breathe:",
                    "🤣 VIRAL COMEDY GOLD - 10M views and counting:",
                    "😂 EVERYONE'S SHARING THIS - you'll die laughing:",
                ]
            }
        }
    
    def _build_engagement_templates(self) -> Dict:
        """Build templates optimized for different engagement goals"""
        
        return {
            "viral_focused": {
                "structure": "{explosive_hook}\n\n{curiosity_gap}\n\n{value_delivery}\n\n{viral_cta}",
                "elements": {
                    "curiosity_gap": [
                        "But here's the twist nobody talks about:",
                        "The surprising part? This actually works:",
                        "Plot twist - this changes everything:",
                    ]
                }
            },
            "educational": {
                "structure": "{teaching_hook}\n\n{problem_statement}\n\n{solution_steps}\n\n{learning_cta}",
                "elements": {
                    "problem_statement": [
                        "Here's the problem most people face:",
                        "The biggest mistake I see everywhere:",
                        "Why traditional methods don't work:",
                    ]
                }
            },
            "storytelling": {
                "structure": "{story_hook}\n\n{context_setting}\n\n{conflict_resolution}\n\n{lesson_learned}\n\n{story_cta}",
                "elements": {
                    "context_setting": [
                        "Let me paint the picture:",
                        "Here's how it all started:",
                        "Picture this scenario:",
                    ]
                }
            }
        }
    
    def _build_niche_expertise(self) -> Dict:
        """Build niche-specific expertise for better content generation"""
        
        return {
            "fitness": {
                "key_concepts": ["form", "progressive overload", "recovery", "nutrition", "consistency"],
                "common_problems": ["plateau", "injury", "motivation", "time constraints", "results"],
                "viral_topics": ["transformation", "before/after", "quick workouts", "home exercises", "nutrition hacks"],
                "expert_language": ["reps", "sets", "PRs", "macros", "compound movements", "isolation"],
                "trending_terms": ["75 Hard", "hot girl walks", "12-3-30", "pilates princess", "gym anxiety"]
            },
            "business": {
                "key_concepts": ["scaling", "automation", "revenue", "productivity", "systems"],
                "common_problems": ["burnout", "cash flow", "team management", "competition", "growth"],
                "viral_topics": ["passive income", "side hustles", "productivity hacks", "success stories", "failures"],
                "expert_language": ["KPIs", "ROI", "conversion", "funnel", "ARR", "CAC", "LTV"],
                "trending_terms": ["solopreneur", "creator economy", "AI automation", "remote work", "digital nomad"]
            },
            "technology": {
                "key_concepts": ["innovation", "disruption", "efficiency", "automation", "integration"],
                "common_problems": ["complexity", "security", "adoption", "cost", "obsolescence"],
                "viral_topics": ["AI breakthroughs", "app reviews", "life hacks", "productivity tools", "future predictions"],
                "expert_language": ["API", "cloud", "SaaS", "ML", "blockchain", "IoT"],
                "trending_terms": ["ChatGPT", "no-code", "AI agents", "Web3", "metaverse", "quantum computing"]
            }
        }
    
    def _select_content_strategy(self, viral_score: int, platform: str, niche: str) -> str:
        """Select optimal content strategy based on viral potential and platform"""
        
        if viral_score > 70:
            return "viral_focused"
        elif platform in ["youtube_shorts", "instagram"] and niche in ["business", "fitness"]:
            return "educational"
        else:
            return "storytelling"
    
    def _generate_multiple_hooks(self, niche: str, viral_score: int, platform: str, count: int) -> List[str]:
        """Generate multiple hook options and select the best ones"""
        
        hooks_db = self.viral_hooks_database.get(niche, self.viral_hooks_database["fitness"])
        
        if viral_score > 60:
            intensity = "high_intensity"
        elif viral_score > 30:
            intensity = "medium_intensity"
        else:
            intensity = "low_intensity"
        
        available_hooks = hooks_db.get(intensity, hooks_db["medium_intensity"])
        
        # Generate variations and select best ones
        hooks = []
        for _ in range(count):
            base_hook = random.choice(available_hooks)
            
            # Add platform-specific optimizations
            if platform == "tiktok" and not base_hook.startswith("🚨"):
                base_hook = f"⚡ {base_hook}"
            elif platform == "instagram" and len(base_hook) < 50:
                base_hook += " Let me explain..."
            
            hooks.append(base_hook)
        
        return hooks
    
    def _select_best_hook(self, hook_options: List[str], engagement_style: str) -> str:
        """Select the best hook based on engagement style and scoring"""
        
        scored_hooks = []
        for hook in hook_options:
            score = self._score_hook_effectiveness(hook, engagement_style)
            scored_hooks.append((hook, score))
        
        scored_hooks.sort(key=lambda x: x[1], reverse=True)
        return scored_hooks[0][0]
    
    def _score_hook_effectiveness(self, hook: str, engagement_style: str) -> int:
        """Score hook effectiveness based on engagement triggers"""
        
        score = 0
        hook_lower = hook.lower()
        
        # Urgency indicators
        urgency_words = ["now", "today", "immediately", "urgent", "breaking", "alert"]
        score += sum(5 for word in urgency_words if word in hook_lower)
        
        # Curiosity triggers
        curiosity_words = ["secret", "hack", "trick", "revealed", "nobody knows", "hidden"]
        score += sum(8 for word in curiosity_words if word in hook_lower)
        
        # Social proof
        social_words = ["everyone", "viral", "trending", "millions", "thousands"]
        score += sum(6 for word in social_words if word in hook_lower)
        
        # Emotional triggers
        emotion_words = ["amazing", "incredible", "shocking", "unbelievable", "insane"]
        score += sum(4 for word in emotion_words if word in hook_lower)
        
        # Emojis (engagement boost)
        emoji_count = len(re.findall(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]', hook))
        score += emoji_count * 3
        
        # Length optimization (platform dependent)
        if len(hook) > 30 and len(hook) < 80:
            score += 5
        
        return score
    
    def _generate_advanced_content(self, video_data: Dict, platform: str, 
                                  niche: str, strategy: str) -> str:
        """Generate sophisticated main content using niche expertise"""
        
        expertise = self.niche_expertise.get(niche, self.niche_expertise["fitness"])
        template = self.engagement_templates.get(strategy, self.engagement_templates["viral_focused"])
        
        title = video_data.get("title", "")
        description = video_data.get("description", "")
        
        # Extract key insights using niche expertise
        key_concepts = [concept for concept in expertise["key_concepts"] 
                       if concept.lower() in f"{title} {description}".lower()]
        
        # Generate content based on strategy
        if strategy == "educational":
            content = self._generate_educational_content(title, description, key_concepts, niche)
        elif strategy == "storytelling":
            content = self._generate_story_content(title, description, key_concepts, niche)
        else:  # viral_focused
            content = self._generate_viral_content(title, description, key_concepts, niche)
        
        # Platform-specific optimizations
        if platform == "twitter" and len(content) > 180:
            content = content[:180] + "... (thread below) 🧵"
        elif platform == "tiktok" and len(content) > 100:
            content = content[:100] + "..."
        
        return content
    
    def _generate_educational_content(self, title: str, description: str, 
                                    key_concepts: List[str], niche: str) -> str:
        """Generate educational-focused content"""
        
        templates = [
            "Here's what most people get wrong about {concept}: {insight}. The better approach? {solution}.",
            "Let me break down {concept} for you: {insight}. This changes everything because {reason}.",
            "The truth about {concept} that nobody talks about: {insight}. Here's why it matters: {solution}."
        ]
        
        concept = random.choice(key_concepts) if key_concepts else niche
        insight = f"the key insight from this {niche} content"
        solution = f"applying this {concept} strategy correctly"
        reason = f"it addresses the core {niche} challenge"
        
        template = random.choice(templates)
        return template.format(concept=concept, insight=insight, solution=solution, reason=reason)
    
    def _generate_story_content(self, title: str, description: str,
                               key_concepts: List[str], niche: str) -> str:
        """Generate story-focused content"""
        
        story_templates = [
            "I used to struggle with {challenge} until I discovered {solution}. The results? {outcome}. Game changer.",
            "Plot twist: What everyone thinks about {concept} is wrong. Here's what actually works: {insight}.",
            "True story: I tried this {concept} approach and the results blew my mind. Here's what happened: {outcome}."
        ]
        
        concept = random.choice(key_concepts) if key_concepts else niche
        challenge = f"{niche} challenges"
        solution = f"this {concept} method"
        outcome = "incredible transformation"
        insight = f"the real {concept} secret"
        
        template = random.choice(story_templates)
        return template.format(
            challenge=challenge, solution=solution, outcome=outcome,
            concept=concept, insight=insight
        )
    
    def _generate_viral_content(self, title: str, description: str,
                               key_concepts: List[str], niche: str) -> str:
        """Generate viral-focused content with maximum engagement potential"""
        
        viral_templates = [
            "This {niche} hack is breaking the internet: {insight}. Try it and thank me later! 🔥",
            "POV: You discover the {concept} secret that {niche} experts don't want you to know 👀",
            "Wait... did this just solve the biggest {niche} problem? The answer is YES. 🤯"
        ]
        
        concept = random.choice(key_concepts) if key_concepts else "technique"
        insight = f"the game-changing {concept}"
        
        template = random.choice(viral_templates)
        return template.format(niche=niche, concept=concept, insight=insight)
    
    def _generate_smart_cta(self, platform: str, niche: str, engagement_style: str, viral_score: int) -> str:
        """Generate intelligent call-to-action based on context"""
        
        ctas = {
            "instagram": {
                "high_viral": [
                    "Save this before Instagram hides it! 📌 Tag 3 friends who need this!",
                    "Double tap if this blew your mind! 🤯 Share your results in comments!",
                    "This is going viral for a reason! ⚡ Follow for more game-changers!"
                ],
                "medium_viral": [
                    "What's your experience with this? Drop it below! 👇",
                    "Save for later and tag someone who needs this! ✨",
                    "Follow for more {niche} insights like this! 🔥"
                ]
            },
            "tiktok": {
                "high_viral": [
                    "Duet this with your results! 🔥",
                    "Follow for more viral {niche}! ⚡",
                    "Share if this helped! 💫"
                ]
            }
        }
        
        platform_ctas = ctas.get(platform, ctas["instagram"])
        viral_level = "high_viral" if viral_score > 50 else "medium_viral"
        
        available_ctas = platform_ctas.get(viral_level, platform_ctas.get("medium_viral", ["Follow for more!"]))
        cta = random.choice(available_ctas)
        
        return cta.format(niche=niche)
    
    def _generate_optimized_hashtags(self, video_data: Dict, platform: str, 
                                   niche: str, viral_score: int) -> List[str]:
        """Generate optimized hashtags with trending analysis"""
        
        config = self.platform_configs.get(platform, self.platform_configs["instagram"])
        optimal_count = config["optimal_hashtags"]
        
        if isinstance(optimal_count, tuple):
            count = random.randint(optimal_count[0], optimal_count[1])
        else:
            count = optimal_count
        
        # Build hashtag strategy
        hashtags = []
        
        # Niche-specific hashtags (40%)
        niche_hashtags = self._get_niche_hashtags(niche)
        hashtags.extend(niche_hashtags[:max(1, count // 2)])
        
        # Viral/trending hashtags (30%)
        viral_hashtags = self._get_viral_hashtags(viral_score)
        hashtags.extend(viral_hashtags[:max(1, count // 3)])
        
        # Platform-specific hashtags (20%)
        platform_hashtags = self._get_platform_hashtags(platform)
        hashtags.extend(platform_hashtags[:max(1, count // 5)])
        
        # Content-specific hashtags (10%)
        content_hashtags = self._extract_content_hashtags(video_data, niche)
        hashtags.extend(content_hashtags[:max(1, count // 10)])
        
        # Remove duplicates and optimize
        unique_hashtags = list(dict.fromkeys(hashtags))
        
        # Ensure we hit the target count
        while len(unique_hashtags) < count:
            backup_tags = ["#content", "#viral", "#trending", "#discover"]
            unique_hashtags.extend([tag for tag in backup_tags if tag not in unique_hashtags])
            if len(unique_hashtags) >= count:
                break
        
        return unique_hashtags[:count]
    
    def _extract_content_hashtags(self, video_data: Dict, niche: str) -> List[str]:
        """Extract hashtags from video content analysis"""
        
        title = video_data.get("title", "").lower()
        description = video_data.get("description", "").lower()
        text = f"{title} {description}"
        
        content_tags = []
        
        # Extract topic-specific tags
        if "transformation" in text or "before" in text or "after" in text:
            content_tags.append("#transformation")
        if "workout" in text or "exercise" in text:
            content_tags.append("#workout")
        if "hack" in text or "tip" in text:
            content_tags.append("#hack")
        if "challenge" in text:
            content_tags.append("#challenge")
        if "tutorial" in text or "how to" in text:
            content_tags.append("#tutorial")
        
        return content_tags
    
    def _get_niche_hashtags(self, niche: str) -> List[str]:
        """Enhanced niche hashtags with trending analysis"""
        
        enhanced_niche_hashtags = {
            "fitness": [
                "#fitness", "#workout", "#gym", "#health", "#fitnessmotivation", 
                "#exercise", "#training", "#muscle", "#strength", "#cardio",
                "#transformation", "#fitfam", "#bodybuilding", "#weightloss", "#gains"
            ],
            "business": [
                "#business", "#entrepreneur", "#success", "#mindset", "#hustle", 
                "#startup", "#leadership", "#motivation", "#productivity", "#growth",
                "#businessowner", "#entrepreneurlife", "#success", "#strategy", "#innovation"
            ],
            "technology": [
                "#tech", "#technology", "#innovation", "#ai", "#future", "#digital",
                "#artificialintelligence", "#automation", "#software", "#programming",
                "#techreview", "#gadgets", "#startup", "#innovation", "#cybersecurity"
            ],
            "comedy": [
                "#comedy", "#funny", "#humor", "#memes", "#lol", "#jokes",
                "#standup", "#viral", "#entertainment", "#laughs", "#hilarious",
                "#comedian", "#sketch", "#parody", "#sarcasm"
            ]
        }
        
        return enhanced_niche_hashtags.get(niche, enhanced_niche_hashtags["fitness"])
    
    def _get_viral_hashtags(self, viral_score: int) -> List[str]:
        """Get viral hashtags based on scoring tiers"""
        
        if viral_score > 70:
            return ["#viral", "#trending", "#fyp", "#exploding", "#breakinginternet"]
        elif viral_score > 50:
            return ["#trending", "#viral", "#fyp", "#popular", "#hot"]
        elif viral_score > 30:
            return ["#fyp", "#trending", "#discover", "#explore", "#new"]
        else:
            return ["#discover", "#new", "#explore", "#fresh", "#content"]
    
    def _get_platform_hashtags(self, platform: str) -> List[str]:
        """Enhanced platform-specific hashtags"""
        
        enhanced_platform_hashtags = {
            "instagram": ["#reels", "#instagram", "#insta", "#ig", "#reelsinstagram", "#instareels"],
            "tiktok": ["#fyp", "#foryou", "#tiktok", "#viral", "#foryoupage", "#trending"],
            "youtube_shorts": ["#shorts", "#youtube", "#youtubeshorts", "#shortsvideo", "#ytshorts"],
            "twitter": ["#twitter", "#tweet", "#x", "#trending"]
        }
        
        return enhanced_platform_hashtags.get(platform, [])
    
    def _combine_and_optimize(self, hook: str, content: str, cta: str, max_length: int) -> str:
        """Intelligently combine elements and optimize for length"""
        
        # Calculate space allocation
        hook_space = len(hook) + 2  # +2 for line breaks
        cta_space = len(cta) + 2
        content_space = max_length - hook_space - cta_space - 10  # -10 buffer
        
        # Truncate content if needed
        if len(content) > content_space:
            content = content[:content_space - 3] + "..."
        
        combined = f"{hook}\n\n{content}\n\n{cta}"
        
        # Final length check
        if len(combined) > max_length:
            combined = combined[:max_length - 3] + "..."
        
        return combined
    
    def _generate_posting_recommendations(self, platform: str, viral_score: int) -> Dict:
        """Generate smart posting recommendations"""
        
        config = self.platform_configs.get(platform, self.platform_configs["instagram"])
        
        recommendations = {
            "optimal_times": config.get("peak_times", ["12:00", "18:00"]),
            "engagement_boost": [],
            "platform_tips": []
        }
        
        # Viral score based recommendations
        if viral_score > 60:
            recommendations["engagement_boost"].append("Post immediately - high viral potential")
            recommendations["engagement_boost"].append("Consider boosting/promoting this post")
        
        # Platform-specific tips
        if platform == "instagram":
            recommendations["platform_tips"].extend([
                "Use Instagram Reels format for maximum reach",
                "Add captions for accessibility",
                "Engage with comments in first hour"
            ])
        elif platform == "tiktok":
            recommendations["platform_tips"].extend([
                "Use trending sounds for better reach",
                "Post during peak hours: 6-10 PM",
                "Engage with trending challenges"
            ])
        
        return recommendations
    
    def _calculate_optimization_score(self, caption: str, hashtags: List[str], 
                                    platform: str, viral_score: int) -> int:
        """Calculate overall optimization score for the post"""
        
        score = 0
        
        # Caption quality (40 points)
        if len(caption) > 50:  # Good length
            score += 10
        if any(emoji in caption for emoji in ["🔥", "💪", "⚡", "🚀", "💎"]):  # Engaging emojis
            score += 5
        if "?" in caption:  # Engagement question
            score += 5
        if any(word in caption.lower() for word in ["secret", "hack", "viral", "amazing"]):  # Viral triggers
            score += 10
        if caption.count("\n") >= 2:  # Good formatting
            score += 5
        if len(caption.split()) >= 15:  # Substantial content
            score += 5
        
        # Hashtag optimization (30 points)
        config = self.platform_configs.get(platform, self.platform_configs["instagram"])
        optimal_range = config["optimal_hashtags"]
        if isinstance(optimal_range, tuple):
            if optimal_range[0] <= len(hashtags) <= optimal_range[1]:
                score += 15
        if any("#viral" in tag or "#trending" in tag for tag in hashtags):
            score += 10
        if any("#fyp" in tag or "#explore" in tag for tag in hashtags):
            score += 5
        
        # Viral potential bonus (30 points)
        if viral_score > 70:
            score += 30
        elif viral_score > 50:
            score += 20
        elif viral_score > 30:
            score += 10
        
        return min(score, 100)  # Cap at 100

def main():
    """Test the enhanced content AI system"""
    ai = EnhancedContentAI()
    
    # Mock video data with high viral potential
    video_data = {
        "title": "This 30-Second Fitness Transformation Will Blow Your Mind - Going Viral!",
        "description": "Amazing workout hack that fitness trainers don't want you to know. This simple exercise technique burns fat 10x faster and builds muscle in record time. Millions of people are sharing this incredible transformation method.",
        "viral_score": 85,
        "url": "https://example.com/viral-fitness-video"
    }
    
    print("🧠 Testing Enhanced Content AI Generation...")
    print("=" * 60)
    
    # Test enhanced post generation
    platforms = ["instagram", "tiktok", "youtube_shorts", "twitter"]
    
    for platform in platforms:
        print(f"\n🚀 {platform.upper()} - ENHANCED POST:")
        post = ai.generate_advanced_post(video_data, platform, "fitness", "viral")
        
        print(f"Platform: {post['platform']}")
        print(f"Optimization Score: {post['optimization_score']}/100")
        print(f"Content Strategy: {post['content_strategy']}")
        print(f"\nCaption:\n{post['caption']}")
        print(f"\nHashtags: {' '.join(post['hashtags'])}")
        
        print(f"\n📊 Posting Recommendations:")
        for tip in post['posting_recommendations']['platform_tips']:
            print(f"   • {tip}")
        
        print(f"\n🎯 Hook Options Generated:")
        for i, hook in enumerate(post['hook_options'], 1):
            print(f"   {i}. {hook}")
        print(f"   ✅ Selected: {post['selected_hook']}")
        
        print("-" * 60)

if __name__ == "__main__":
    main()