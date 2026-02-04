#!/usr/bin/env python3
"""
SociaClip AI - Intelligent Scheduling System  
Advanced scheduling with viral optimization, audience analysis, and platform algorithm timing
"""

import json
import random
from datetime import datetime, timedelta, time
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

@dataclass
class ScheduleSlot:
    """Represents a scheduled posting slot with optimization data"""
    time: str
    platform: str
    expected_engagement: float
    viral_multiplier: float
    audience_overlap: float
    competition_level: str
    recommendation_score: int

class IntelligentScheduler:
    """Advanced scheduling system with viral optimization and audience intelligence"""
    
    def __init__(self):
        self.platform_algorithms = self._build_algorithm_intelligence()
        self.audience_patterns = self._build_audience_patterns()
        self.viral_timing_windows = self._build_viral_windows()
        self.content_type_optimization = self._build_content_optimization()
    
    def _build_algorithm_intelligence(self) -> Dict:
        """Build platform algorithm intelligence for optimal timing"""
        
        return {
            "instagram": {
                "algorithm_preference": "engagement_velocity",  # Fast early engagement
                "golden_window": 60,  # minutes for maximum algorithm boost
                "peak_algorithm_times": ["11:00", "14:00", "17:00", "20:00"],
                "low_competition_windows": ["08:00", "10:00", "13:00", "16:00", "19:00"],
                "engagement_decay": {
                    "0-1h": 1.0,    # 100% algorithm priority
                    "1-3h": 0.8,    # 80% algorithm priority  
                    "3-6h": 0.6,    # 60% algorithm priority
                    "6-24h": 0.3    # 30% algorithm priority
                },
                "viral_boost_threshold": 50  # viral score needed for algorithm boost
            },
            "tiktok": {
                "algorithm_preference": "completion_rate",  # Focus on watch time
                "golden_window": 120,  # minutes for FYP consideration
                "peak_algorithm_times": ["18:00", "19:00", "20:00", "21:00", "22:00"],
                "low_competition_windows": ["15:00", "17:00", "23:00"],
                "engagement_decay": {
                    "0-2h": 1.0,
                    "2-4h": 0.9,
                    "4-8h": 0.7,
                    "8-24h": 0.4
                },
                "viral_boost_threshold": 40
            },
            "youtube_shorts": {
                "algorithm_preference": "click_through_rate",
                "golden_window": 180,  # minutes for Shorts shelf consideration
                "peak_algorithm_times": ["14:00", "16:00", "18:00", "20:00"],
                "low_competition_windows": ["10:00", "12:00", "15:00", "17:00"],
                "engagement_decay": {
                    "0-3h": 1.0,
                    "3-6h": 0.85,
                    "6-12h": 0.7,
                    "12-48h": 0.5
                },
                "viral_boost_threshold": 60
            },
            "twitter": {
                "algorithm_preference": "real_time_engagement",
                "golden_window": 30,  # minutes for trending consideration
                "peak_algorithm_times": ["09:00", "12:00", "15:00", "18:00"],
                "low_competition_windows": ["10:00", "11:00", "14:00", "16:00"],
                "engagement_decay": {
                    "0-30m": 1.0,
                    "30m-2h": 0.7,
                    "2h-6h": 0.4,
                    "6h-24h": 0.2
                },
                "viral_boost_threshold": 35
            }
        }
    
    def _build_audience_patterns(self) -> Dict:
        """Build audience behavior patterns for different niches and times"""
        
        return {
            "fitness": {
                "morning_motivation": {
                    "times": ["06:00", "07:00", "08:00"],
                    "engagement_multiplier": 1.4,
                    "content_preference": "motivational_workout"
                },
                "lunch_break": {
                    "times": ["12:00", "13:00"],
                    "engagement_multiplier": 1.2,
                    "content_preference": "quick_tips"
                },
                "evening_workout": {
                    "times": ["17:00", "18:00", "19:00"],
                    "engagement_multiplier": 1.6,
                    "content_preference": "workout_routines"
                },
                "night_inspiration": {
                    "times": ["21:00", "22:00"],
                    "engagement_multiplier": 1.3,
                    "content_preference": "transformation_stories"
                }
            },
            "business": {
                "morning_productivity": {
                    "times": ["07:00", "08:00", "09:00"],
                    "engagement_multiplier": 1.5,
                    "content_preference": "productivity_hacks"
                },
                "midday_break": {
                    "times": ["12:00", "13:00", "14:00"],
                    "engagement_multiplier": 1.3,
                    "content_preference": "success_stories"
                },
                "evening_learning": {
                    "times": ["19:00", "20:00", "21:00"],
                    "engagement_multiplier": 1.4,
                    "content_preference": "educational_content"
                }
            },
            "technology": {
                "morning_news": {
                    "times": ["08:00", "09:00"],
                    "engagement_multiplier": 1.3,
                    "content_preference": "tech_news"
                },
                "afternoon_reviews": {
                    "times": ["15:00", "16:00", "17:00"],
                    "engagement_multiplier": 1.4,
                    "content_preference": "product_reviews"
                },
                "evening_tutorials": {
                    "times": ["20:00", "21:00", "22:00"],
                    "engagement_multiplier": 1.2,
                    "content_preference": "how_to_guides"
                }
            }
        }
    
    def _build_viral_windows(self) -> Dict:
        """Build viral timing windows when content is most likely to go viral"""
        
        return {
            "weekday_viral_windows": [
                {"start": "11:00", "end": "13:00", "multiplier": 1.4, "reason": "Lunch scroll sessions"},
                {"start": "17:00", "end": "19:00", "multiplier": 1.6, "reason": "Post-work entertainment"},
                {"start": "20:00", "end": "22:00", "multiplier": 1.8, "reason": "Prime entertainment hours"}
            ],
            "weekend_viral_windows": [
                {"start": "10:00", "end": "12:00", "multiplier": 1.3, "reason": "Weekend morning leisure"},
                {"start": "14:00", "end": "16:00", "multiplier": 1.5, "reason": "Afternoon browsing"},
                {"start": "19:00", "end": "23:00", "multiplier": 2.0, "reason": "Weekend entertainment peak"}
            ],
            "viral_content_boost": {
                "high_viral": {"min_score": 70, "time_multiplier": 1.5},
                "medium_viral": {"min_score": 50, "time_multiplier": 1.2},
                "low_viral": {"min_score": 30, "time_multiplier": 1.0}
            }
        }
    
    def _build_content_optimization(self) -> Dict:
        """Build content type optimization for different posting times"""
        
        return {
            "morning": {
                "optimal_content": ["motivation", "tips", "education"],
                "avoid_content": ["entertainment", "heavy_topics"],
                "engagement_boost": 1.2
            },
            "midday": {
                "optimal_content": ["quick_tips", "inspiration", "news"],
                "avoid_content": ["long_form", "complex_tutorials"],
                "engagement_boost": 1.1
            },
            "evening": {
                "optimal_content": ["entertainment", "stories", "transformation"],
                "avoid_content": ["work_related", "productivity"],
                "engagement_boost": 1.4
            },
            "night": {
                "optimal_content": ["inspiration", "relaxation", "reflection"],
                "avoid_content": ["high_energy", "workout_intensive"],
                "engagement_boost": 1.3
            }
        }
    
    def generate_optimal_schedule(self, posts: List[Dict], target_date: str = None) -> List[Dict]:
        """Generate optimal posting schedule with viral timing and audience optimization"""
        
        if not target_date:
            target_date = datetime.now().strftime("%Y-%m-%d")
        
        scheduled_posts = []
        
        # Analyze posts and create schedule recommendations
        for i, post in enumerate(posts):
            platform = post.get("platform", "instagram")
            niche = post.get("niche", "fitness")
            viral_score = post.get("viral_score", 0)
            
            # Generate multiple time slot options
            time_options = self._generate_time_options(platform, niche, viral_score)
            
            # Select best time slot avoiding conflicts
            best_slot = self._select_best_slot(time_options, scheduled_posts, platform)
            
            # Add scheduling intelligence
            scheduled_post = post.copy()
            scheduled_post.update({
                "scheduled_date": target_date,
                "scheduled_time": best_slot.time,
                "scheduling_intelligence": {
                    "expected_engagement": best_slot.expected_engagement,
                    "viral_multiplier": best_slot.viral_multiplier,
                    "audience_overlap": best_slot.audience_overlap,
                    "competition_level": best_slot.competition_level,
                    "recommendation_score": best_slot.recommendation_score,
                    "algorithm_optimization": self._get_algorithm_tips(platform, best_slot.time),
                    "posting_strategy": self._get_posting_strategy(platform, niche, viral_score)
                }
            })
            
            scheduled_posts.append(scheduled_post)
        
        # Sort by scheduled time
        scheduled_posts.sort(key=lambda x: x["scheduled_time"])
        
        return scheduled_posts
    
    def _generate_time_options(self, platform: str, niche: str, viral_score: int) -> List[ScheduleSlot]:
        """Generate optimal time slot options for a specific post"""
        
        algorithm_data = self.platform_algorithms.get(platform, self.platform_algorithms["instagram"])
        audience_data = self.audience_patterns.get(niche, self.audience_patterns["fitness"])
        
        time_options = []
        
        # Platform algorithm optimal times
        for time_str in algorithm_data["peak_algorithm_times"]:
            slot = self._create_schedule_slot(time_str, platform, niche, viral_score, "algorithm")
            time_options.append(slot)
        
        # Low competition windows
        for time_str in algorithm_data["low_competition_windows"]:
            slot = self._create_schedule_slot(time_str, platform, niche, viral_score, "low_competition")
            time_options.append(slot)
        
        # Audience behavior optimal times
        for period, data in audience_data.items():
            for time_str in data["times"]:
                slot = self._create_schedule_slot(time_str, platform, niche, viral_score, "audience")
                slot.expected_engagement *= data["engagement_multiplier"]
                time_options.append(slot)
        
        # Viral window optimization
        viral_windows = self._get_viral_windows_for_day(datetime.now().weekday())
        for window in viral_windows:
            window_times = self._generate_times_in_window(window["start"], window["end"])
            for time_str in window_times:
                slot = self._create_schedule_slot(time_str, platform, niche, viral_score, "viral")
                slot.viral_multiplier *= window["multiplier"]
                time_options.append(slot)
        
        # Remove duplicates and sort by recommendation score
        unique_slots = self._deduplicate_slots(time_options)
        unique_slots.sort(key=lambda x: x.recommendation_score, reverse=True)
        
        return unique_slots[:10]  # Top 10 options
    
    def _create_schedule_slot(self, time_str: str, platform: str, niche: str, 
                            viral_score: int, optimization_type: str) -> ScheduleSlot:
        """Create a schedule slot with intelligence data"""
        
        # Calculate base engagement expectation
        hour = int(time_str.split(":")[0])
        base_engagement = self._calculate_base_engagement(hour, platform, niche)
        
        # Calculate viral multiplier
        viral_multiplier = self._calculate_viral_multiplier(viral_score, time_str, platform)
        
        # Calculate audience overlap (how crowded this time slot is)
        audience_overlap = self._calculate_audience_overlap(time_str, platform, niche)
        
        # Determine competition level
        competition_level = self._determine_competition_level(time_str, platform)
        
        # Calculate overall recommendation score
        recommendation_score = self._calculate_recommendation_score(
            base_engagement, viral_multiplier, audience_overlap, competition_level, optimization_type
        )
        
        return ScheduleSlot(
            time=time_str,
            platform=platform,
            expected_engagement=base_engagement,
            viral_multiplier=viral_multiplier,
            audience_overlap=audience_overlap,
            competition_level=competition_level,
            recommendation_score=recommendation_score
        )
    
    def _calculate_base_engagement(self, hour: int, platform: str, niche: str) -> float:
        """Calculate expected base engagement for time and platform"""
        
        # Platform-specific engagement patterns
        platform_patterns = {
            "instagram": {
                "peak_hours": [11, 14, 17, 20],
                "good_hours": [8, 10, 13, 16, 19, 21],
                "low_hours": [0, 1, 2, 3, 4, 5, 6, 22, 23]
            },
            "tiktok": {
                "peak_hours": [18, 19, 20, 21, 22],
                "good_hours": [15, 16, 17, 23],
                "low_hours": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            },
            "youtube_shorts": {
                "peak_hours": [14, 16, 18, 20],
                "good_hours": [10, 12, 15, 17, 19, 21],
                "low_hours": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 22, 23]
            },
            "twitter": {
                "peak_hours": [9, 12, 15, 18],
                "good_hours": [8, 10, 11, 13, 14, 16, 17, 19],
                "low_hours": [0, 1, 2, 3, 4, 5, 6, 7, 20, 21, 22, 23]
            }
        }
        
        pattern = platform_patterns.get(platform, platform_patterns["instagram"])
        
        if hour in pattern["peak_hours"]:
            base = 0.9
        elif hour in pattern["good_hours"]:
            base = 0.7
        else:
            base = 0.4
        
        # Niche-specific adjustments
        niche_multipliers = {
            "fitness": {"morning": 1.2, "evening": 1.3, "night": 1.1},
            "business": {"morning": 1.4, "midday": 1.2, "evening": 1.1},
            "technology": {"morning": 1.1, "afternoon": 1.3, "evening": 1.2}
        }
        
        if 6 <= hour < 12:
            period = "morning"
        elif 12 <= hour < 17:
            period = "midday" if "midday" in niche_multipliers.get(niche, {}) else "afternoon"
        elif 17 <= hour < 21:
            period = "evening"
        else:
            period = "night"
        
        niche_data = niche_multipliers.get(niche, {"morning": 1.0, "midday": 1.0, "afternoon": 1.0, "evening": 1.0, "night": 1.0})
        niche_mult = niche_data.get(period, 1.0)
        
        return base * niche_mult
    
    def _calculate_viral_multiplier(self, viral_score: int, time_str: str, platform: str) -> float:
        """Calculate viral potential multiplier for specific time"""
        
        # Base viral multiplier from score
        if viral_score > 70:
            base_viral = 1.8
        elif viral_score > 50:
            base_viral = 1.4
        elif viral_score > 30:
            base_viral = 1.2
        else:
            base_viral = 1.0
        
        # Time-based viral boost
        hour = int(time_str.split(":")[0])
        viral_hours = {
            "instagram": [11, 14, 17, 20],
            "tiktok": [18, 19, 20, 21],
            "youtube_shorts": [16, 18, 20],
            "twitter": [12, 15, 18]
        }
        
        platform_viral_hours = viral_hours.get(platform, viral_hours["instagram"])
        
        if hour in platform_viral_hours:
            time_boost = 1.3
        else:
            time_boost = 1.0
        
        return base_viral * time_boost
    
    def _calculate_audience_overlap(self, time_str: str, platform: str, niche: str) -> float:
        """Calculate how much audience overlap exists at this time (crowding factor)"""
        
        hour = int(time_str.split(":")[0])
        
        # High-competition hours (everyone posts here)
        high_competition_hours = {
            "instagram": [12, 18, 20],
            "tiktok": [19, 20, 21],
            "youtube_shorts": [18, 20],
            "twitter": [12, 18]
        }
        
        platform_busy_hours = high_competition_hours.get(platform, high_competition_hours["instagram"])
        
        if hour in platform_busy_hours:
            return 0.8  # High overlap = lower individual post visibility
        elif hour in [hour + 1 for hour in platform_busy_hours] + [hour - 1 for hour in platform_busy_hours]:
            return 0.6  # Medium overlap
        else:
            return 0.3  # Low overlap = better visibility
    
    def _determine_competition_level(self, time_str: str, platform: str) -> str:
        """Determine competition level for posting time"""
        
        hour = int(time_str.split(":")[0])
        
        high_competition_hours = {
            "instagram": [12, 17, 18, 20],
            "tiktok": [19, 20, 21],
            "youtube_shorts": [18, 20],
            "twitter": [12, 15, 18]
        }
        
        platform_busy = high_competition_hours.get(platform, high_competition_hours["instagram"])
        
        if hour in platform_busy:
            return "high"
        elif any(abs(hour - busy_hour) <= 1 for busy_hour in platform_busy):
            return "medium"
        else:
            return "low"
    
    def _calculate_recommendation_score(self, engagement: float, viral_mult: float, 
                                      overlap: float, competition: str, opt_type: str) -> int:
        """Calculate overall recommendation score for a time slot"""
        
        score = 0
        
        # Base engagement score (40 points)
        score += engagement * 40
        
        # Viral multiplier bonus (30 points)
        score += (viral_mult - 1.0) * 30
        
        # Low overlap bonus (20 points) - less crowded is better
        score += (1.0 - overlap) * 20
        
        # Competition penalty/bonus (10 points)
        competition_scores = {"low": 10, "medium": 5, "high": 0}
        score += competition_scores.get(competition, 5)
        
        # Optimization type bonus
        type_bonuses = {
            "viral": 5,
            "algorithm": 3, 
            "audience": 4,
            "low_competition": 2
        }
        score += type_bonuses.get(opt_type, 0)
        
        return min(int(score), 100)  # Cap at 100
    
    def _get_viral_windows_for_day(self, weekday: int) -> List[Dict]:
        """Get viral windows for specific day of week"""
        
        if weekday < 5:  # Weekday (0-4)
            return self.viral_timing_windows["weekday_viral_windows"]
        else:  # Weekend (5-6)
            return self.viral_timing_windows["weekend_viral_windows"]
    
    def _generate_times_in_window(self, start_time: str, end_time: str) -> List[str]:
        """Generate time slots within a viral window"""
        
        start_hour = int(start_time.split(":")[0])
        end_hour = int(end_time.split(":")[0])
        
        times = []
        for hour in range(start_hour, end_hour + 1):
            times.append(f"{hour:02d}:00")
            if hour < end_hour:  # Don't add :30 for the last hour
                times.append(f"{hour:02d}:30")
        
        return times
    
    def _deduplicate_slots(self, slots: List[ScheduleSlot]) -> List[ScheduleSlot]:
        """Remove duplicate time slots, keeping the highest scoring ones"""
        
        time_to_slot = {}
        for slot in slots:
            if slot.time not in time_to_slot or slot.recommendation_score > time_to_slot[slot.time].recommendation_score:
                time_to_slot[slot.time] = slot
        
        return list(time_to_slot.values())
    
    def _select_best_slot(self, time_options: List[ScheduleSlot], 
                         scheduled_posts: List[Dict], platform: str) -> ScheduleSlot:
        """Select the best time slot avoiding conflicts"""
        
        # Get already scheduled times
        scheduled_times = set(post.get("scheduled_time") for post in scheduled_posts)
        
        # Filter out conflicting times (within 30 minutes)
        available_slots = []
        for slot in time_options:
            slot_time = datetime.strptime(slot.time, "%H:%M").time()
            
            conflict = False
            for scheduled_time_str in scheduled_times:
                if not scheduled_time_str:
                    continue
                scheduled_time = datetime.strptime(scheduled_time_str, "%H:%M").time()
                
                # Check if within 30 minutes
                slot_minutes = slot_time.hour * 60 + slot_time.minute
                scheduled_minutes = scheduled_time.hour * 60 + scheduled_time.minute
                
                if abs(slot_minutes - scheduled_minutes) < 30:
                    conflict = True
                    break
            
            if not conflict:
                available_slots.append(slot)
        
        if not available_slots:
            # If all slots conflict, return the best one anyway (emergency fallback)
            return time_options[0] if time_options else ScheduleSlot("12:00", platform, 0.5, 1.0, 0.5, "medium", 50)
        
        # Return the highest scoring available slot
        return max(available_slots, key=lambda x: x.recommendation_score)
    
    def _get_algorithm_tips(self, platform: str, scheduled_time: str) -> List[str]:
        """Get algorithm optimization tips for specific platform and time"""
        
        algorithm_data = self.platform_algorithms.get(platform, self.platform_algorithms["instagram"])
        
        tips = []
        
        # Golden window tip
        golden_window = algorithm_data["golden_window"]
        tips.append(f"Engage actively in first {golden_window} minutes for algorithm boost")
        
        # Platform-specific tips
        if platform == "instagram":
            tips.extend([
                "Use Reels format for maximum algorithm preference",
                "Add captions for accessibility boost",
                "Use trending audio if applicable",
                "Engage with comments immediately after posting"
            ])
        elif platform == "tiktok":
            tips.extend([
                "Focus on high completion rate - keep content engaging throughout",
                "Use trending sounds for FYP algorithm boost", 
                "Hook viewers in first 3 seconds",
                "Encourage rewatches for algorithm signals"
            ])
        elif platform == "youtube_shorts":
            tips.extend([
                "Optimize thumbnail even for Shorts",
                "Use compelling titles for click-through rate",
                "Add end screen to encourage more views",
                "Use trending topics in description"
            ])
        elif platform == "twitter":
            tips.extend([
                "Tweet during high-activity periods for engagement",
                "Use trending hashtags sparingly",
                "Engage with replies quickly for algorithm boost",
                "Consider quote tweets of trending topics"
            ])
        
        return tips
    
    def _get_posting_strategy(self, platform: str, niche: str, viral_score: int) -> Dict:
        """Get comprehensive posting strategy for the content"""
        
        strategy = {
            "pre_post": [],
            "post_publish": [],
            "engagement_tactics": [],
            "viral_amplification": []
        }
        
        # Pre-posting strategy
        strategy["pre_post"].extend([
            "Prepare engaging caption with hook",
            "Research trending hashtags for the day",
            "Have response templates ready for comments"
        ])
        
        # Post-publish strategy
        strategy["post_publish"].extend([
            "Share to Stories (Instagram) or create response videos",
            "Engage with first 10 comments personally",
            "Share in relevant communities/groups if appropriate"
        ])
        
        # Engagement tactics
        strategy["engagement_tactics"].extend([
            "Ask questions to encourage comments",
            "Use polls in Stories to drive traffic back to post",
            "Create follow-up content based on comments"
        ])
        
        # Viral amplification (if high viral score)
        if viral_score > 60:
            strategy["viral_amplification"].extend([
                "Consider paid promotion for first few hours",
                "Share across all platforms simultaneously",
                "Reach out to micro-influencers for shares",
                "Monitor trending hashtags to join conversations"
            ])
        
        return strategy
    
    def analyze_schedule_performance(self, scheduled_posts: List[Dict]) -> Dict:
        """Analyze the overall schedule for optimization opportunities"""
        
        analysis = {
            "total_posts": len(scheduled_posts),
            "platform_distribution": {},
            "time_distribution": {},
            "viral_potential_score": 0,
            "optimization_score": 0,
            "recommendations": []
        }
        
        # Platform distribution
        for post in scheduled_posts:
            platform = post.get("platform", "unknown")
            analysis["platform_distribution"][platform] = analysis["platform_distribution"].get(platform, 0) + 1
        
        # Time distribution
        for post in scheduled_posts:
            time_slot = post.get("scheduled_time", "unknown")
            hour = time_slot.split(":")[0] if ":" in time_slot else "unknown"
            analysis["time_distribution"][f"{hour}:xx"] = analysis["time_distribution"].get(f"{hour}:xx", 0) + 1
        
        # Overall viral potential
        viral_scores = [post.get("viral_score", 0) for post in scheduled_posts]
        analysis["viral_potential_score"] = sum(viral_scores) / len(viral_scores) if viral_scores else 0
        
        # Overall optimization score
        optimization_scores = [
            post.get("scheduling_intelligence", {}).get("recommendation_score", 50) 
            for post in scheduled_posts
        ]
        analysis["optimization_score"] = sum(optimization_scores) / len(optimization_scores) if optimization_scores else 50
        
        # Generate recommendations
        if analysis["optimization_score"] < 70:
            analysis["recommendations"].append("Consider rescheduling some posts to higher-scoring time slots")
        
        if analysis["viral_potential_score"] > 60:
            analysis["recommendations"].append("High viral potential detected - consider paid promotion")
        
        if len(set(post.get("scheduled_time") for post in scheduled_posts)) < len(scheduled_posts):
            analysis["recommendations"].append("Some posts scheduled too close together - spread out timing")
        
        return analysis

def main():
    """Test the intelligent scheduling system"""
    scheduler = IntelligentScheduler()
    
    # Mock posts with different viral potentials
    test_posts = [
        {
            "platform": "instagram", 
            "niche": "fitness", 
            "viral_score": 85,
            "caption": "Amazing workout transformation!",
            "content_type": "transformation"
        },
        {
            "platform": "tiktok",
            "niche": "fitness", 
            "viral_score": 45,
            "caption": "Quick fitness tip for busy people",
            "content_type": "tips"
        },
        {
            "platform": "youtube_shorts",
            "niche": "business",
            "viral_score": 65, 
            "caption": "Business hack that changed everything",
            "content_type": "educational"
        },
        {
            "platform": "twitter",
            "niche": "technology",
            "viral_score": 35,
            "caption": "Cool new AI tool discovery",
            "content_type": "news"
        }
    ]
    
    print("🧠 Testing Intelligent Scheduling System...")
    print("=" * 60)
    
    # Generate optimal schedule
    scheduled_posts = scheduler.generate_optimal_schedule(test_posts)
    
    print(f"\n📅 OPTIMIZED POSTING SCHEDULE:")
    print(f"{'Time':<8} {'Platform':<15} {'Viral Score':<12} {'Opt Score':<10} {'Competition':<12}")
    print("-" * 70)
    
    for post in scheduled_posts:
        intelligence = post.get("scheduling_intelligence", {})
        print(f"{post['scheduled_time']:<8} {post['platform']:<15} {post['viral_score']:<12} "
              f"{intelligence.get('recommendation_score', 0):<10} {intelligence.get('competition_level', 'unknown'):<12}")
    
    print(f"\n🎯 DETAILED SCHEDULING INTELLIGENCE:")
    for i, post in enumerate(scheduled_posts, 1):
        intelligence = post.get("scheduling_intelligence", {})
        print(f"\n📱 Post {i}: {post['platform']} at {post['scheduled_time']}")
        print(f"   Expected Engagement: {intelligence.get('expected_engagement', 0):.1f}")
        print(f"   Viral Multiplier: {intelligence.get('viral_multiplier', 1):.1f}x")
        print(f"   Competition Level: {intelligence.get('competition_level', 'unknown')}")
        print(f"   Recommendation Score: {intelligence.get('recommendation_score', 0)}/100")
        
        # Show algorithm tips
        algorithm_tips = intelligence.get("algorithm_optimization", [])
        if algorithm_tips:
            print(f"   🤖 Algorithm Tips:")
            for tip in algorithm_tips[:2]:  # Show first 2 tips
                print(f"      • {tip}")
    
    # Analyze overall schedule
    print(f"\n📊 SCHEDULE PERFORMANCE ANALYSIS:")
    analysis = scheduler.analyze_schedule_performance(scheduled_posts)
    print(f"   Total Posts: {analysis['total_posts']}")
    print(f"   Average Viral Potential: {analysis['viral_potential_score']:.1f}")
    print(f"   Average Optimization Score: {analysis['optimization_score']:.1f}/100")
    
    if analysis['recommendations']:
        print(f"   💡 Recommendations:")
        for rec in analysis['recommendations']:
            print(f"      • {rec}")

if __name__ == "__main__":
    main()