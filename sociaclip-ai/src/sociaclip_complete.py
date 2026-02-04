#!/usr/bin/env python3
"""
SociaClip AI - Complete Integration Module
Brings together all components for full automated social media content generation and scheduling
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from trend_scanner import TrendScanner
from enhanced_content_ai import EnhancedContentAI
from intelligent_scheduler import IntelligentScheduler

class SociaClipComplete:
    """Complete SociaClip AI system with all advanced features integrated"""
    
    def __init__(self, config: Dict = None):
        self.config = config or self._get_default_config()
        
        # Initialize all components
        self.trend_scanner = TrendScanner(self.config.get("brave_api_key"))
        self.content_ai = EnhancedContentAI()
        self.scheduler = IntelligentScheduler()
        
        # Performance tracking
        self.session_stats = {
            "start_time": datetime.now(),
            "videos_discovered": 0,
            "posts_generated": 0,
            "posts_scheduled": 0,
            "optimization_score": 0
        }
        
    def _get_default_config(self) -> Dict:
        """Get comprehensive default configuration"""
        return {
            "brave_api_key": "BSAgcgZWW_ZL3hFjAxJ7vfug8SbHhJf",
            "posts_per_day": 5,
            "target_niches": ["fitness", "business", "technology", "comedy"],
            "platforms": ["instagram", "tiktok", "youtube_shorts", "twitter"],
            "content_strategy": {
                "viral_threshold": 50,
                "engagement_style": "viral",
                "optimization_priority": "viral_potential"
            },
            "scheduling_strategy": {
                "avoid_conflicts": True,
                "optimize_for_algorithms": True,
                "prioritize_viral_windows": True,
                "minimum_gap_minutes": 30
            },
            "quality_filters": {
                "min_viral_score": 30,
                "min_optimization_score": 60,
                "max_caption_length_ratio": 0.9
            }
        }
    
    def run_complete_workflow(self, niche: str = None, target_date: str = None) -> Dict:
        """Run the complete workflow from discovery to scheduling"""
        
        print("🚀 Starting SociaClip AI Complete Workflow...")
        workflow_results = {
            "status": "running",
            "start_time": datetime.now().isoformat(),
            "niche": niche or "mixed",
            "target_date": target_date or datetime.now().strftime("%Y-%m-%d"),
            "phases": {}
        }
        
        try:
            # Phase 1: Content Discovery with Intelligence
            print("\n📡 Phase 1: Intelligent Content Discovery")
            discovery_results = self._run_discovery_phase(niche)
            workflow_results["phases"]["discovery"] = discovery_results
            print(f"   ✅ Discovered {len(discovery_results['trending_videos'])} trending videos")
            
            # Phase 2: Advanced Content Generation  
            print("\n🧠 Phase 2: Advanced AI Content Generation")
            generation_results = self._run_generation_phase(discovery_results["selected_content"], niche)
            workflow_results["phases"]["generation"] = generation_results
            print(f"   ✅ Generated {len(generation_results['generated_posts'])} optimized posts")
            
            # Phase 3: Intelligent Scheduling
            print("\n⏰ Phase 3: Intelligent Scheduling Optimization")
            scheduling_results = self._run_scheduling_phase(generation_results["generated_posts"], target_date)
            workflow_results["phases"]["scheduling"] = scheduling_results
            print(f"   ✅ Scheduled {len(scheduling_results['scheduled_posts'])} posts optimally")
            
            # Phase 4: Quality Assurance & Analytics
            print("\n🔍 Phase 4: Quality Assurance & Performance Prediction")
            qa_results = self._run_qa_phase(scheduling_results["scheduled_posts"])
            workflow_results["phases"]["quality_assurance"] = qa_results
            print(f"   ✅ Quality score: {qa_results['overall_quality_score']}/100")
            
            # Phase 5: Export & Deployment Ready
            print("\n📤 Phase 5: Export & Deployment Preparation")
            export_results = self._run_export_phase(scheduling_results["scheduled_posts"])
            workflow_results["phases"]["export"] = export_results
            print(f"   ✅ Exported to {export_results['export_file']}")
            
            # Final Results
            workflow_results.update({
                "status": "completed",
                "end_time": datetime.now().isoformat(),
                "duration_seconds": (datetime.now() - datetime.fromisoformat(workflow_results["start_time"])).seconds,
                "final_posts": scheduling_results["scheduled_posts"],
                "performance_prediction": qa_results["performance_prediction"],
                "deployment_ready": True
            })
            
            print(f"\n🎉 Complete Workflow Finished Successfully!")
            print(f"   📊 Total Posts: {len(scheduling_results['scheduled_posts'])}")
            print(f"   🎯 Average Quality: {qa_results['overall_quality_score']}/100") 
            print(f"   ⚡ Processing Time: {workflow_results['duration_seconds']} seconds")
            
            return workflow_results
            
        except Exception as e:
            workflow_results.update({
                "status": "error",
                "error": str(e),
                "end_time": datetime.now().isoformat()
            })
            print(f"❌ Workflow Error: {e}")
            return workflow_results
    
    def _run_discovery_phase(self, niche: str = None) -> Dict:
        """Run intelligent content discovery phase"""
        
        results = {
            "phase": "discovery",
            "niches_scanned": [],
            "trending_videos": [],
            "selected_content": [],
            "discovery_intelligence": {}
        }
        
        # Determine niches to scan
        niches_to_scan = [niche] if niche else self.config["target_niches"]
        results["niches_scanned"] = niches_to_scan
        
        # Scan each niche with enhanced intelligence
        all_videos = []
        for scan_niche in niches_to_scan:
            try:
                print(f"   🔍 Scanning {scan_niche} content...")
                videos = self.trend_scanner.search_trending_videos(scan_niche)
                
                # Add discovery intelligence
                for video in videos:
                    video["discovered_niche"] = scan_niche
                    video["discovery_timestamp"] = datetime.now().isoformat()
                
                all_videos.extend(videos)
                self.session_stats["videos_discovered"] += len(videos)
                
            except Exception as e:
                print(f"   ⚠️  Warning: Error scanning {scan_niche}: {e}")
                continue
        
        results["trending_videos"] = all_videos
        
        # Intelligent content selection
        selected_content = self._intelligent_content_selection(all_videos)
        results["selected_content"] = selected_content
        
        # Discovery intelligence analysis
        results["discovery_intelligence"] = self._analyze_discovery_results(all_videos, selected_content)
        
        return results
    
    def _run_generation_phase(self, selected_content: List[Dict], niche: str) -> Dict:
        """Run advanced content generation phase"""
        
        results = {
            "phase": "generation",
            "generated_posts": [],
            "generation_intelligence": {},
            "platform_distribution": {}
        }
        
        platforms = self.config["platforms"]
        posts_per_platform = max(1, len(selected_content) // len(platforms))
        
        generated_posts = []
        platform_counts = {platform: 0 for platform in platforms}
        
        video_index = 0
        for platform in platforms:
            for i in range(posts_per_platform):
                if video_index >= len(selected_content):
                    break
                
                video = selected_content[video_index]
                
                try:
                    print(f"   🎨 Generating {platform} content (viral score: {video.get('viral_score', 0)})")
                    
                    # Generate advanced post
                    post = self.content_ai.generate_advanced_post(
                        video, platform, niche or "mixed", self.config["content_strategy"]["engagement_style"]
                    )
                    
                    # Add metadata
                    post.update({
                        "source_video": video,
                        "niche": niche or video.get("discovered_niche", "mixed"),
                        "generation_timestamp": datetime.now().isoformat()
                    })
                    
                    generated_posts.append(post)
                    platform_counts[platform] += 1
                    video_index += 1
                    
                except Exception as e:
                    print(f"   ⚠️  Warning: Generation error for {platform}: {e}")
                    video_index += 1
                    continue
        
        results["generated_posts"] = generated_posts
        results["platform_distribution"] = platform_counts
        results["generation_intelligence"] = self._analyze_generation_results(generated_posts)
        
        self.session_stats["posts_generated"] = len(generated_posts)
        
        return results
    
    def _run_scheduling_phase(self, generated_posts: List[Dict], target_date: str = None) -> Dict:
        """Run intelligent scheduling phase"""
        
        results = {
            "phase": "scheduling", 
            "scheduled_posts": [],
            "scheduling_intelligence": {},
            "conflicts_resolved": 0
        }
        
        print(f"   📅 Optimizing schedule for {len(generated_posts)} posts")
        
        # Generate optimal schedule
        scheduled_posts = self.scheduler.generate_optimal_schedule(generated_posts, target_date)
        
        # Analyze scheduling results
        scheduling_analysis = self.scheduler.analyze_schedule_performance(scheduled_posts)
        
        results.update({
            "scheduled_posts": scheduled_posts,
            "scheduling_intelligence": scheduling_analysis,
            "conflicts_resolved": len(generated_posts) - len(scheduled_posts)  # If any were dropped due to conflicts
        })
        
        self.session_stats["posts_scheduled"] = len(scheduled_posts)
        
        return results
    
    def _run_qa_phase(self, scheduled_posts: List[Dict]) -> Dict:
        """Run quality assurance and performance prediction phase"""
        
        results = {
            "phase": "quality_assurance",
            "overall_quality_score": 0,
            "individual_scores": [],
            "performance_prediction": {},
            "quality_issues": [],
            "optimization_suggestions": []
        }
        
        # Quality scoring for each post
        quality_scores = []
        for post in scheduled_posts:
            score = self._calculate_post_quality_score(post)
            quality_scores.append(score)
            
            if score < self.config["quality_filters"]["min_optimization_score"]:
                results["quality_issues"].append({
                    "post_id": post.get("id", "unknown"),
                    "platform": post.get("platform"),
                    "issue": f"Low quality score: {score}/100"
                })
        
        results["individual_scores"] = quality_scores
        results["overall_quality_score"] = sum(quality_scores) / len(quality_scores) if quality_scores else 0
        
        # Performance prediction
        results["performance_prediction"] = self._predict_performance(scheduled_posts)
        
        # Optimization suggestions
        results["optimization_suggestions"] = self._generate_optimization_suggestions(scheduled_posts, results)
        
        return results
    
    def _run_export_phase(self, scheduled_posts: List[Dict]) -> Dict:
        """Run export and deployment preparation phase"""
        
        results = {
            "phase": "export",
            "export_file": "",
            "deployment_packages": {},
            "api_ready": False
        }
        
        # Create export directory
        export_dir = "exports"
        os.makedirs(export_dir, exist_ok=True)
        
        # Generate comprehensive export
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        export_filename = f"sociaclip_complete_{timestamp}.json"
        export_path = os.path.join(export_dir, export_filename)
        
        # Comprehensive export data
        export_data = {
            "export_info": {
                "generated_at": datetime.now().isoformat(),
                "sociaclip_version": "1.0.0-complete",
                "total_posts": len(scheduled_posts),
                "target_date": scheduled_posts[0].get("scheduled_date") if scheduled_posts else None
            },
            "scheduled_posts": scheduled_posts,
            "deployment_instructions": self._generate_deployment_instructions(scheduled_posts),
            "monitoring_setup": self._generate_monitoring_setup(),
            "api_endpoints": self._generate_api_endpoints()
        }
        
        # Write export file
        with open(export_path, 'w') as f:
            json.dump(export_data, f, indent=2, default=str)
        
        results.update({
            "export_file": export_path,
            "deployment_packages": {
                "json_export": export_path,
                "api_ready": True,
                "monitoring_config": "included"
            },
            "api_ready": True
        })
        
        return results
    
    def _intelligent_content_selection(self, all_videos: List[Dict]) -> List[Dict]:
        """Intelligently select the best content for posting"""
        
        # Filter by minimum viral score
        min_score = self.config["quality_filters"]["min_viral_score"]
        qualified_videos = [v for v in all_videos if v.get("viral_score", 0) >= min_score]
        
        # Sort by viral potential and diversity
        qualified_videos.sort(key=lambda x: x.get("viral_score", 0), reverse=True)
        
        # Ensure diversity across niches if scanning multiple
        if len(set(v.get("discovered_niche") for v in qualified_videos)) > 1:
            selected = []
            niches_used = set()
            posts_needed = self.config["posts_per_day"]
            
            # First pass: one from each niche
            for video in qualified_videos:
                niche = video.get("discovered_niche")
                if niche not in niches_used and len(selected) < posts_needed:
                    selected.append(video)
                    niches_used.add(niche)
            
            # Second pass: fill remaining slots with highest scores
            remaining_needed = posts_needed - len(selected)
            remaining_videos = [v for v in qualified_videos if v not in selected]
            selected.extend(remaining_videos[:remaining_needed])
            
            return selected
        else:
            # Single niche - just take top scorers
            return qualified_videos[:self.config["posts_per_day"]]
    
    def _analyze_discovery_results(self, all_videos: List[Dict], selected_videos: List[Dict]) -> Dict:
        """Analyze discovery phase results"""
        
        return {
            "total_discovered": len(all_videos),
            "total_selected": len(selected_videos),
            "selection_rate": len(selected_videos) / len(all_videos) if all_videos else 0,
            "average_viral_score": sum(v.get("viral_score", 0) for v in selected_videos) / len(selected_videos) if selected_videos else 0,
            "niche_distribution": {
                niche: len([v for v in selected_videos if v.get("discovered_niche") == niche])
                for niche in set(v.get("discovered_niche") for v in selected_videos)
            },
            "quality_metrics": {
                "high_viral_content": len([v for v in selected_videos if v.get("viral_score", 0) > 70]),
                "medium_viral_content": len([v for v in selected_videos if 50 <= v.get("viral_score", 0) <= 70]),
                "low_viral_content": len([v for v in selected_videos if v.get("viral_score", 0) < 50])
            }
        }
    
    def _analyze_generation_results(self, generated_posts: List[Dict]) -> Dict:
        """Analyze content generation results"""
        
        return {
            "total_generated": len(generated_posts),
            "average_optimization_score": sum(p.get("optimization_score", 0) for p in generated_posts) / len(generated_posts) if generated_posts else 0,
            "content_strategy_distribution": {
                strategy: len([p for p in generated_posts if p.get("content_strategy") == strategy])
                for strategy in set(p.get("content_strategy") for p in generated_posts)
            },
            "engagement_style_distribution": {
                style: len([p for p in generated_posts if p.get("engagement_style") == style]) 
                for style in set(p.get("engagement_style") for p in generated_posts)
            },
            "platform_optimization": {
                platform: {
                    "count": len([p for p in generated_posts if p.get("platform") == platform]),
                    "avg_score": sum(p.get("optimization_score", 0) for p in generated_posts if p.get("platform") == platform) / len([p for p in generated_posts if p.get("platform") == platform]) if [p for p in generated_posts if p.get("platform") == platform] else 0
                }
                for platform in set(p.get("platform") for p in generated_posts)
            }
        }
    
    def _calculate_post_quality_score(self, post: Dict) -> int:
        """Calculate comprehensive quality score for a post"""
        
        score = 0
        
        # Content quality (40 points)
        optimization_score = post.get("optimization_score", 0)
        score += optimization_score * 0.4
        
        # Scheduling quality (30 points)  
        scheduling_intel = post.get("scheduling_intelligence", {})
        recommendation_score = scheduling_intel.get("recommendation_score", 0)
        score += recommendation_score * 0.3
        
        # Viral potential (20 points)
        viral_score = post.get("viral_score", 0)
        if viral_score > 70:
            score += 20
        elif viral_score > 50:
            score += 15
        elif viral_score > 30:
            score += 10
        else:
            score += 5
        
        # Completeness check (10 points)
        required_fields = ["caption", "hashtags", "scheduled_time", "platform"]
        completeness = sum(1 for field in required_fields if post.get(field))
        score += (completeness / len(required_fields)) * 10
        
        return min(int(score), 100)
    
    def _predict_performance(self, scheduled_posts: List[Dict]) -> Dict:
        """Predict performance of the scheduled posts"""
        
        predictions = {
            "total_expected_engagement": 0,
            "viral_potential_posts": 0,
            "platform_predictions": {},
            "time_slot_analysis": {},
            "success_probability": 0
        }
        
        total_engagement = 0
        viral_potential_count = 0
        
        for post in scheduled_posts:
            # Calculate expected engagement
            viral_score = post.get("viral_score", 0)
            optimization_score = post.get("optimization_score", 0)
            scheduling_intel = post.get("scheduling_intelligence", {})
            expected_engagement = scheduling_intel.get("expected_engagement", 0.5)
            viral_multiplier = scheduling_intel.get("viral_multiplier", 1.0)
            
            # Predict engagement level
            predicted_engagement = expected_engagement * viral_multiplier * (optimization_score / 100)
            total_engagement += predicted_engagement
            
            if viral_score > 60:
                viral_potential_count += 1
            
            # Platform-specific predictions
            platform = post.get("platform")
            if platform not in predictions["platform_predictions"]:
                predictions["platform_predictions"][platform] = {
                    "posts": 0,
                    "expected_engagement": 0,
                    "viral_potential": 0
                }
            
            predictions["platform_predictions"][platform]["posts"] += 1
            predictions["platform_predictions"][platform]["expected_engagement"] += predicted_engagement
            predictions["platform_predictions"][platform]["viral_potential"] += 1 if viral_score > 60 else 0
        
        predictions.update({
            "total_expected_engagement": total_engagement,
            "viral_potential_posts": viral_potential_count,
            "success_probability": min(95, max(20, int(total_engagement * 30 + viral_potential_count * 10)))
        })
        
        return predictions
    
    def _generate_optimization_suggestions(self, scheduled_posts: List[Dict], qa_results: Dict) -> List[str]:
        """Generate optimization suggestions based on QA analysis"""
        
        suggestions = []
        
        # Overall quality suggestions
        if qa_results["overall_quality_score"] < 80:
            suggestions.append("Consider regenerating content with higher viral score videos for better quality")
        
        # Viral potential suggestions
        viral_posts = len([p for p in scheduled_posts if p.get("viral_score", 0) > 60])
        if viral_posts < len(scheduled_posts) * 0.3:
            suggestions.append("Increase viral content ratio - target more high-scoring trending videos")
        
        # Platform distribution suggestions
        platform_counts = {}
        for post in scheduled_posts:
            platform = post.get("platform")
            platform_counts[platform] = platform_counts.get(platform, 0) + 1
        
        if max(platform_counts.values()) > len(scheduled_posts) * 0.6:
            suggestions.append("Consider more balanced platform distribution for broader reach")
        
        # Timing suggestions
        scheduled_times = [post.get("scheduled_time") for post in scheduled_posts]
        if len(set(scheduled_times)) < len(scheduled_times) * 0.8:
            suggestions.append("Spread out posting times more for better individual post visibility")
        
        return suggestions
    
    def _generate_deployment_instructions(self, scheduled_posts: List[Dict]) -> Dict:
        """Generate deployment instructions for the scheduled posts"""
        
        return {
            "posting_workflow": [
                "Review generated content for brand alignment",
                "Prepare any visual assets (videos/images)",
                "Schedule posts using platform native schedulers or third-party tools", 
                "Monitor first-hour engagement for algorithm optimization",
                "Engage with comments and responses actively"
            ],
            "platform_specific": {
                platform: {
                    "posts_count": len([p for p in scheduled_posts if p.get("platform") == platform]),
                    "optimal_times": list(set(p.get("scheduled_time") for p in scheduled_posts if p.get("platform") == platform)),
                    "special_instructions": self._get_platform_deployment_instructions(platform)
                }
                for platform in set(p.get("platform") for p in scheduled_posts)
            },
            "monitoring_requirements": [
                "Track engagement rates within first 2 hours",
                "Monitor hashtag performance", 
                "Watch for viral breakthrough indicators",
                "Document what works for optimization"
            ]
        }
    
    def _get_platform_deployment_instructions(self, platform: str) -> List[str]:
        """Get platform-specific deployment instructions"""
        
        instructions = {
            "instagram": [
                "Use Reels format for maximum reach",
                "Add alt text for accessibility",
                "Cross-post to Stories",
                "Enable notifications for comments"
            ],
            "tiktok": [
                "Use trending sounds when possible",
                "Add captions for accessibility", 
                "Engage with trending hashtags",
                "Monitor FYP performance"
            ],
            "youtube_shorts": [
                "Create eye-catching thumbnails",
                "Add end screens for subscriber growth",
                "Use YouTube Analytics for performance tracking",
                "Optimize titles for search"
            ],
            "twitter": [
                "Pin important tweets",
                "Use Twitter Analytics for insights",
                "Engage with trending topics",
                "Consider thread follow-ups"
            ]
        }
        
        return instructions.get(platform, ["Follow platform best practices"])
    
    def _generate_monitoring_setup(self) -> Dict:
        """Generate monitoring and analytics setup instructions"""
        
        return {
            "key_metrics": [
                "Engagement rate (likes, comments, shares)",
                "Reach and impressions", 
                "Click-through rates",
                "Hashtag performance",
                "Best posting times validation"
            ],
            "tracking_schedule": {
                "immediate": "First 30 minutes after posting",
                "short_term": "First 24 hours performance",
                "medium_term": "7-day performance analysis", 
                "long_term": "Monthly trend analysis"
            },
            "optimization_triggers": {
                "high_performance": "Analyze and replicate successful elements",
                "low_performance": "Review and adjust content strategy",
                "viral_breakthrough": "Amplify with paid promotion",
                "algorithm_changes": "Adapt posting strategy"
            }
        }
    
    def _generate_api_endpoints(self) -> Dict:
        """Generate API endpoints for integration"""
        
        return {
            "content_generation": "/api/v1/generate",
            "scheduling": "/api/v1/schedule", 
            "analytics": "/api/v1/analytics",
            "webhooks": {
                "post_published": "/api/v1/webhooks/published",
                "engagement_milestone": "/api/v1/webhooks/engagement",
                "viral_alert": "/api/v1/webhooks/viral"
            }
        }

def main():
    """Test the complete SociaClip AI system"""
    print("🚀 SociaClip AI Complete System Test")
    print("=" * 60)
    
    # Initialize complete system
    sociaclip = SociaClipComplete()
    
    # Run complete workflow
    results = sociaclip.run_complete_workflow("fitness")
    
    # Display results summary
    print(f"\n📊 COMPLETE WORKFLOW RESULTS:")
    print(f"   Status: {results['status']}")
    print(f"   Duration: {results.get('duration_seconds', 0)} seconds")
    print(f"   Posts Generated: {len(results.get('final_posts', []))}")
    
    if results.get('performance_prediction'):
        pred = results['performance_prediction']
        print(f"   Expected Engagement: {pred.get('total_expected_engagement', 0):.1f}")
        print(f"   Success Probability: {pred.get('success_probability', 0)}%")
        print(f"   Viral Potential Posts: {pred.get('viral_potential_posts', 0)}")
    
    # Show quality analysis
    if results.get('phases', {}).get('quality_assurance'):
        qa = results['phases']['quality_assurance']
        print(f"   Overall Quality: {qa.get('overall_quality_score', 0):.1f}/100")
        
        if qa.get('optimization_suggestions'):
            print(f"   💡 Optimization Suggestions:")
            for suggestion in qa['optimization_suggestions'][:3]:
                print(f"      • {suggestion}")

if __name__ == "__main__":
    main()