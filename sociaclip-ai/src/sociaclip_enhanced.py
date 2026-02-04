#!/usr/bin/env python3
"""
SociaClip AI - Enhanced Complete System
Integration of video processing with content generation and scheduling
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional
from trend_scanner import TrendScanner
from enhanced_content_ai import EnhancedContentAI
from intelligent_scheduler import IntelligentScheduler
from video_processor import VideoProcessor

class SociaClipEnhanced:
    """Enhanced SociaClip AI with complete video processing integration"""
    
    def __init__(self, config: Dict = None):
        self.config = config or self._get_default_config()
        
        # Initialize all components
        self.trend_scanner = TrendScanner(self.config.get("brave_api_key"))
        self.content_ai = EnhancedContentAI()
        self.scheduler = IntelligentScheduler()
        self.video_processor = VideoProcessor()
        
    def _get_default_config(self) -> Dict:
        """Get enhanced configuration"""
        return {
            "brave_api_key": "BSAgcgZWW_ZL3hFjAxJ7vfug8SbHhJf",
            "posts_per_day": 5,
            "target_niches": ["fitness", "business", "technology", "comedy"],
            "platforms": ["instagram", "tiktok", "youtube_shorts", "twitter"],
            "video_processing": {
                "enabled": True,
                "max_clips_per_video": 3,
                "preferred_clip_duration": 15,
                "quality_threshold": 60
            },
            "content_enhancement": {
                "use_video_insights": True,
                "optimize_for_clips": True,
                "viral_optimization": True
            }
        }
    
    def run_enhanced_workflow(self, niche: str = None, target_date: str = None) -> Dict:
        """Run enhanced workflow with video processing"""
        
        print("🚀 SociaClip AI Enhanced - Full Video Processing Workflow")
        print("=" * 60)
        
        workflow_results = {
            "status": "running",
            "start_time": datetime.now().isoformat(),
            "niche": niche or "mixed",
            "target_date": target_date or datetime.now().strftime("%Y-%m-%d"),
            "phases": {},
            "video_processing_enabled": True
        }
        
        try:
            # Phase 1: Enhanced Content Discovery
            print("\n📡 Phase 1: Enhanced Content Discovery with Video Analysis")
            discovery_results = self._run_enhanced_discovery(niche)
            workflow_results["phases"]["discovery"] = discovery_results
            print(f"   ✅ Discovered {len(discovery_results['processed_videos'])} videos with full analysis")
            
            # Phase 2: Video Processing & Clip Extraction
            print("\n🎬 Phase 2: Video Processing & Clip Extraction")
            processing_results = self._run_video_processing(discovery_results["selected_videos"])
            workflow_results["phases"]["video_processing"] = processing_results
            print(f"   ✅ Processed {len(processing_results['processed_videos'])} videos")
            print(f"   ✅ Extracted {processing_results['total_clips']} clips")
            
            # Phase 3: Enhanced Content Generation
            print("\n🧠 Phase 3: Enhanced Content Generation with Video Insights")
            generation_results = self._run_enhanced_generation(processing_results, niche)
            workflow_results["phases"]["generation"] = generation_results
            print(f"   ✅ Generated {len(generation_results['enhanced_posts'])} video-optimized posts")
            
            # Phase 4: Intelligent Scheduling with Clip Optimization
            print("\n⏰ Phase 4: Intelligent Scheduling with Clip Optimization")
            scheduling_results = self._run_enhanced_scheduling(generation_results["enhanced_posts"], target_date)
            workflow_results["phases"]["scheduling"] = scheduling_results
            print(f"   ✅ Scheduled {len(scheduling_results['scheduled_posts'])} posts with clip recommendations")
            
            # Phase 5: Enhanced Export with Video Assets
            print("\n📤 Phase 5: Enhanced Export with Video Assets")
            export_results = self._run_enhanced_export(scheduling_results["scheduled_posts"])
            workflow_results["phases"]["export"] = export_results
            print(f"   ✅ Exported complete package to {export_results['export_file']}")
            
            # Final Results
            workflow_results.update({
                "status": "completed",
                "end_time": datetime.now().isoformat(),
                "duration_seconds": (datetime.now() - datetime.fromisoformat(workflow_results["start_time"])).seconds,
                "final_posts": scheduling_results["scheduled_posts"],
                "video_insights": processing_results["insights_summary"],
                "deployment_ready": True,
                "clips_ready": processing_results["clips_ready_for_use"]
            })
            
            print(f"\n🎉 Enhanced Workflow Complete!")
            print(f"   📊 Posts: {len(scheduling_results['scheduled_posts'])}")
            print(f"   🎬 Clips: {processing_results['total_clips']}")
            print(f"   ⚡ Time: {workflow_results['duration_seconds']} seconds")
            
            return workflow_results
            
        except Exception as e:
            workflow_results.update({
                "status": "error",
                "error": str(e),
                "end_time": datetime.now().isoformat()
            })
            print(f"❌ Enhanced Workflow Error: {e}")
            return workflow_results
    
    def _run_enhanced_discovery(self, niche: str = None) -> Dict:
        """Run discovery with enhanced video selection"""
        
        results = {
            "phase": "enhanced_discovery",
            "videos_found": [],
            "selected_videos": [],
            "processed_videos": [],
            "selection_criteria": {}
        }
        
        # Discover trending videos
        niches_to_scan = [niche] if niche else self.config["target_niches"]
        
        all_videos = []
        for scan_niche in niches_to_scan:
            try:
                print(f"   🔍 Scanning {scan_niche} content...")
                videos = self.trend_scanner.search_trending_videos(scan_niche)
                all_videos.extend(videos)
            except Exception as e:
                print(f"   ⚠️ Warning: {e}")
                continue
        
        results["videos_found"] = all_videos
        
        # Enhanced video selection with processing potential
        selected_videos = self._select_videos_for_processing(all_videos)
        results["selected_videos"] = selected_videos
        
        # Quick video analysis for selection validation
        processed_videos = []
        for video in selected_videos[:5]:  # Process top 5 videos
            if self._is_processable_video(video):
                processed_videos.append(video)
        
        results["processed_videos"] = processed_videos
        results["selection_criteria"] = {
            "total_found": len(all_videos),
            "selected": len(selected_videos),
            "processable": len(processed_videos)
        }
        
        return results
    
    def _select_videos_for_processing(self, videos: List[Dict]) -> List[Dict]:
        """Select videos optimized for processing and clip extraction"""
        
        # Filter for processable videos
        processable_videos = [v for v in videos if self._is_processable_video(v)]
        
        # Sort by viral potential and processing suitability
        processable_videos.sort(key=lambda x: (
            x.get("viral_score", 0),
            self._calculate_processing_potential(x)
        ), reverse=True)
        
        return processable_videos[:self.config["posts_per_day"] * 2]
    
    def _is_processable_video(self, video: Dict) -> bool:
        """Check if video is suitable for processing"""
        
        url = video.get("url", "")
        if not url:
            return False
        
        # Check if URL is from supported platforms
        supported_domains = ["youtube.com", "youtu.be", "tiktok.com"]
        return any(domain in url.lower() for domain in supported_domains)
    
    def _calculate_processing_potential(self, video: Dict) -> int:
        """Calculate how suitable a video is for processing"""
        
        score = 0
        title = video.get("title", "").lower()
        
        # Favor content types that work well as clips
        clip_friendly_keywords = [
            "transformation", "before after", "tutorial", "hack", "tip",
            "challenge", "reaction", "review", "test", "experiment"
        ]
        
        for keyword in clip_friendly_keywords:
            if keyword in title:
                score += 20
        
        # Platform preference (YouTube > TikTok > others)
        url = video.get("url", "").lower()
        if "youtube" in url:
            score += 30
        elif "tiktok" in url:
            score += 20
        
        return score
    
    def _run_video_processing(self, selected_videos: List[Dict]) -> Dict:
        """Process videos and extract clips"""
        
        results = {
            "phase": "video_processing",
            "processed_videos": [],
            "total_clips": 0,
            "clips_by_video": {},
            "processing_errors": [],
            "insights_summary": {},
            "clips_ready_for_use": []
        }
        
        all_clips = []
        processing_summary = []
        
        for video in selected_videos[:3]:  # Process top 3 videos
            video_url = video.get("url")
            if not video_url:
                continue
                
            try:
                print(f"   🎬 Processing: {video.get('title', 'Unknown')[:50]}...")
                
                # Process video with full analysis
                processing_result = self.video_processor.process_video(video_url)
                
                if processing_result["processing_success"]:
                    clips = processing_result.get("clips_extracted", [])
                    
                    # Enhance clips with original video metadata
                    enhanced_clips = self._enhance_clips_with_metadata(clips, video, processing_result)
                    
                    all_clips.extend(enhanced_clips)
                    results["clips_by_video"][video_url] = enhanced_clips
                    
                    processing_summary.append({
                        "video_url": video_url,
                        "title": video.get("title", ""),
                        "clips_extracted": len(clips),
                        "analysis_quality": processing_result.get("analysis_quality", 0),
                        "best_clip_potential": max([c.get("viral_potential", 0) for c in clips]) if clips else 0
                    })
                else:
                    results["processing_errors"].append({
                        "video_url": video_url,
                        "error": processing_result.get("error", "Unknown error")
                    })
                    
            except Exception as e:
                results["processing_errors"].append({
                    "video_url": video_url,
                    "error": str(e)
                })
        
        results.update({
            "processed_videos": processing_summary,
            "total_clips": len(all_clips),
            "clips_ready_for_use": all_clips,
            "insights_summary": self._generate_processing_insights(processing_summary, all_clips)
        })
        
        return results
    
    def _enhance_clips_with_metadata(self, clips: List[Dict], original_video: Dict, processing_result: Dict) -> List[Dict]:
        """Enhance clips with original video metadata and processing insights"""
        
        enhanced_clips = []
        
        for clip in clips:
            enhanced_clip = clip.copy()
            enhanced_clip.update({
                "original_video_metadata": {
                    "title": original_video.get("title", ""),
                    "url": original_video.get("url", ""),
                    "viral_score": original_video.get("viral_score", 0),
                    "discovered_niche": original_video.get("discovered_niche", "")
                },
                "processing_insights": {
                    "content_themes": processing_result.get("content_analysis", {}).get("content_themes", []),
                    "viral_indicators": processing_result.get("content_analysis", {}).get("viral_indicators", {}),
                    "engagement_triggers": processing_result.get("content_analysis", {}).get("engagement_triggers", {})
                },
                "enhanced_metadata": {
                    "generated_at": datetime.now().isoformat(),
                    "processing_quality": processing_result.get("analysis_quality", 0),
                    "ready_for_content_generation": True
                }
            })
            
            enhanced_clips.append(enhanced_clip)
        
        return enhanced_clips
    
    def _generate_processing_insights(self, processing_summary: List[Dict], all_clips: List[Dict]) -> Dict:
        """Generate insights from video processing results"""
        
        if not processing_summary:
            return {"status": "no_videos_processed"}
        
        # Calculate overall metrics
        total_videos = len(processing_summary)
        total_clips = len(all_clips)
        avg_clips_per_video = total_clips / total_videos if total_videos > 0 else 0
        avg_quality = sum(v.get("analysis_quality", 0) for v in processing_summary) / total_videos if total_videos > 0 else 0
        
        # Find best content
        best_video = max(processing_summary, key=lambda x: x.get("best_clip_potential", 0)) if processing_summary else None
        best_clips = sorted(all_clips, key=lambda x: x.get("viral_potential", 0), reverse=True)[:3]
        
        # Platform recommendations
        platform_distribution = {}
        for clip in all_clips:
            for platform in clip.get("suggested_platforms", []):
                platform_distribution[platform] = platform_distribution.get(platform, 0) + 1
        
        return {
            "processing_summary": {
                "videos_processed": total_videos,
                "total_clips_extracted": total_clips,
                "avg_clips_per_video": round(avg_clips_per_video, 1),
                "avg_analysis_quality": round(avg_quality, 1)
            },
            "content_insights": {
                "best_video": best_video,
                "top_clips": [
                    {
                        "description": clip.get("description", ""),
                        "viral_potential": clip.get("viral_potential", 0),
                        "clip_type": clip.get("clip_type", "")
                    } for clip in best_clips
                ]
            },
            "platform_recommendations": platform_distribution,
            "optimization_opportunities": self._identify_optimization_opportunities(all_clips)
        }
    
    def _identify_optimization_opportunities(self, clips: List[Dict]) -> List[str]:
        """Identify optimization opportunities from processed clips"""
        
        opportunities = []
        
        if not clips:
            return ["No clips processed - consider expanding video selection"]
        
        # High potential clips
        high_potential_clips = [c for c in clips if c.get("viral_potential", 0) > 70]
        if len(high_potential_clips) > 2:
            opportunities.append(f"Focus on {len(high_potential_clips)} high-potential clips for maximum impact")
        
        # Platform distribution
        platform_counts = {}
        for clip in clips:
            for platform in clip.get("suggested_platforms", []):
                platform_counts[platform] = platform_counts.get(platform, 0) + 1
        
        if platform_counts:
            best_platform = max(platform_counts, key=platform_counts.get)
            opportunities.append(f"Prioritize {best_platform} - best platform match for your content")
        
        # Content type analysis
        clip_types = [c.get("clip_type") for c in clips]
        most_common_type = max(set(clip_types), key=clip_types.count) if clip_types else None
        if most_common_type:
            opportunities.append(f"Leverage '{most_common_type}' content type - appears most frequently")
        
        return opportunities[:5]  # Return top 5 opportunities
    
    def _run_enhanced_generation(self, processing_results: Dict, niche: str) -> Dict:
        """Generate content enhanced with video processing insights"""
        
        results = {
            "phase": "enhanced_generation",
            "enhanced_posts": [],
            "generation_strategy": "video_optimized"
        }
        
        clips = processing_results.get("clips_ready_for_use", [])
        
        if not clips:
            print("   ⚠️ No clips available, using standard generation")
            # Fallback to standard generation if no clips
            return {"enhanced_posts": [], "fallback_used": True}
        
        # Sort clips by viral potential
        clips.sort(key=lambda x: x.get("viral_potential", 0), reverse=True)
        
        # Generate enhanced posts for top clips
        platforms = self.config["platforms"]
        enhanced_posts = []
        
        clips_used = 0
        for platform in platforms:
            if clips_used >= len(clips):
                break
                
            clip = clips[clips_used]
            
            try:
                print(f"   🎨 Generating enhanced {platform} content from clip...")
                
                # Create enhanced post with video insights
                post = self._generate_video_enhanced_post(clip, platform, niche)
                enhanced_posts.append(post)
                clips_used += 1
                
            except Exception as e:
                print(f"   ⚠️ Warning: Generation error for {platform}: {e}")
                continue
        
        results["enhanced_posts"] = enhanced_posts
        return results
    
    def _generate_video_enhanced_post(self, clip: Dict, platform: str, niche: str) -> Dict:
        """Generate post enhanced with video processing insights"""
        
        # Extract insights from clip
        original_video = clip.get("original_video_metadata", {})
        processing_insights = clip.get("processing_insights", {})
        
        # Create enhanced video data for content generation
        enhanced_video_data = {
            "title": original_video.get("title", ""),
            "description": clip.get("description", ""),
            "viral_score": clip.get("viral_potential", 0),
            "url": original_video.get("url", ""),
            "content_themes": processing_insights.get("content_themes", []),
            "viral_indicators": processing_insights.get("viral_indicators", {}),
            "engagement_triggers": processing_insights.get("engagement_triggers", {}),
            "clip_insights": {
                "clip_type": clip.get("clip_type", ""),
                "duration": clip.get("duration", 15),
                "suggested_platforms": clip.get("suggested_platforms", []),
                "engagement_prediction": clip.get("engagement_prediction", {})
            }
        }
        
        # Generate advanced post with video insights
        post = self.content_ai.generate_advanced_post(
            enhanced_video_data, platform, niche, "viral"
        )
        
        # Enhance post with clip-specific information
        post.update({
            "clip_source": clip,
            "video_enhanced": True,
            "clip_timing": {
                "start_time": clip.get("start_time", 0),
                "duration": clip.get("duration", 15)
            },
            "platform_optimization": clip.get("suggested_platforms", []),
            "video_insights_used": True
        })
        
        return post
    
    def _run_enhanced_scheduling(self, enhanced_posts: List[Dict], target_date: str = None) -> Dict:
        """Schedule posts with clip optimization"""
        
        results = {
            "phase": "enhanced_scheduling",
            "scheduled_posts": [],
            "clip_optimization_applied": True
        }
        
        if not enhanced_posts:
            return results
        
        # Generate optimal schedule with clip considerations
        scheduled_posts = self.scheduler.generate_optimal_schedule(enhanced_posts, target_date)
        
        # Add clip-specific scheduling intelligence
        for post in scheduled_posts:
            clip_source = post.get("clip_source", {})
            
            # Add clip-specific posting recommendations
            scheduling_intel = post.get("scheduling_intelligence", {})
            scheduling_intel.update({
                "clip_optimization": {
                    "clip_type": clip_source.get("clip_type", ""),
                    "duration": clip_source.get("duration", 15),
                    "viral_potential": clip_source.get("viral_potential", 0),
                    "best_platforms": clip_source.get("suggested_platforms", []),
                    "clip_timing_notes": self._generate_clip_timing_notes(clip_source)
                }
            })
            
            post["scheduling_intelligence"] = scheduling_intel
        
        results["scheduled_posts"] = scheduled_posts
        return results
    
    def _generate_clip_timing_notes(self, clip: Dict) -> List[str]:
        """Generate timing notes specific to the clip"""
        
        notes = []
        
        clip_type = clip.get("clip_type", "")
        duration = clip.get("duration", 15)
        viral_potential = clip.get("viral_potential", 0)
        
        if clip_type == "hook":
            notes.append("Post during high-activity hours for maximum hook impact")
        elif clip_type == "transformation":
            notes.append("Consider morning posts for motivation content")
        elif clip_type == "climax":
            notes.append("Evening posts work best for entertainment content")
        
        if duration <= 10:
            notes.append("Short clip - ideal for TikTok prime time")
        elif duration >= 30:
            notes.append("Longer clip - better for YouTube Shorts audience")
        
        if viral_potential > 70:
            notes.append("High viral potential - consider paid promotion boost")
        
        return notes[:3]  # Return top 3 notes
    
    def _run_enhanced_export(self, scheduled_posts: List[Dict]) -> Dict:
        """Export enhanced system with video assets"""
        
        results = {
            "phase": "enhanced_export",
            "export_file": "",
            "video_assets_included": True
        }
        
        # Create export directory
        export_dir = "exports"
        os.makedirs(export_dir, exist_ok=True)
        
        # Generate enhanced export
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        export_filename = f"sociaclip_enhanced_{timestamp}.json"
        export_path = os.path.join(export_dir, export_filename)
        
        # Comprehensive enhanced export
        export_data = {
            "export_info": {
                "generated_at": datetime.now().isoformat(),
                "sociaclip_version": "1.0.0-enhanced",
                "video_processing_enabled": True,
                "total_posts": len(scheduled_posts),
                "clips_included": len([p for p in scheduled_posts if p.get("clip_source")])
            },
            "scheduled_posts": scheduled_posts,
            "video_assets": {
                "clips_metadata": [p.get("clip_source", {}) for p in scheduled_posts if p.get("clip_source")],
                "processing_insights": self._extract_processing_insights_for_export(scheduled_posts)
            },
            "enhanced_deployment": {
                "video_workflow": self._generate_video_deployment_workflow(),
                "clip_management": self._generate_clip_management_instructions(),
                "enhanced_monitoring": self._generate_enhanced_monitoring_setup()
            }
        }
        
        # Write enhanced export
        with open(export_path, 'w') as f:
            json.dump(export_data, f, indent=2, default=str)
        
        results["export_file"] = export_path
        return results
    
    def _extract_processing_insights_for_export(self, scheduled_posts: List[Dict]) -> Dict:
        """Extract processing insights for export"""
        
        insights = {
            "total_clips": len([p for p in scheduled_posts if p.get("clip_source")]),
            "viral_potential_distribution": {},
            "clip_type_distribution": {},
            "platform_optimization": {}
        }
        
        clips = [p.get("clip_source", {}) for p in scheduled_posts if p.get("clip_source")]
        
        # Viral potential distribution
        for clip in clips:
            potential = clip.get("viral_potential", 0)
            if potential > 70:
                insights["viral_potential_distribution"]["high"] = insights["viral_potential_distribution"].get("high", 0) + 1
            elif potential > 50:
                insights["viral_potential_distribution"]["medium"] = insights["viral_potential_distribution"].get("medium", 0) + 1
            else:
                insights["viral_potential_distribution"]["low"] = insights["viral_potential_distribution"].get("low", 0) + 1
        
        # Clip type distribution
        for clip in clips:
            clip_type = clip.get("clip_type", "unknown")
            insights["clip_type_distribution"][clip_type] = insights["clip_type_distribution"].get(clip_type, 0) + 1
        
        return insights
    
    def _generate_video_deployment_workflow(self) -> List[str]:
        """Generate video deployment workflow"""
        
        return [
            "Review generated posts and associated clip metadata",
            "Download or prepare actual video clips based on timing information",
            "Create video assets using provided start_time and duration",
            "Upload posts with video content to respective platforms",
            "Monitor engagement especially for high-viral-potential clips",
            "Analyze performance to optimize future clip selection"
        ]
    
    def _generate_clip_management_instructions(self) -> Dict:
        """Generate clip management instructions"""
        
        return {
            "clip_preparation": [
                "Use provided start_time and duration for precise clip extraction",
                "Maintain original video quality for best results",
                "Add captions or text overlays as suggested in content optimization",
                "Ensure clips match the predicted viral moments"
            ],
            "quality_control": [
                "Verify clips match the described content (hook, climax, etc.)",
                "Check audio quality and visual clarity",
                "Ensure clips are engaging within first 3 seconds",
                "Test clips on target platforms before scheduling"
            ],
            "optimization": [
                "Use high-viral-potential clips during peak posting hours",
                "A/B test different clips from same source video",
                "Monitor which clip types perform best for your audience",
                "Adjust future video selection based on clip performance"
            ]
        }
    
    def _generate_enhanced_monitoring_setup(self) -> Dict:
        """Generate enhanced monitoring setup for video content"""
        
        return {
            "video_metrics": [
                "Clip completion rate (percentage of viewers who watch full clip)",
                "Engagement rate by clip type (hook vs climax vs transformation)",
                "Platform-specific performance (which clips work best where)",
                "Viral breakthrough indicators (rapid sharing, comment spikes)"
            ],
            "clip_analysis": [
                "Track which viral moments predictions were accurate",
                "Monitor correlation between processing quality and actual performance",
                "Analyze which content themes generate most engagement",
                "Identify patterns in successful clip timing and duration"
            ],
            "optimization_triggers": [
                "High-performing clip types should be prioritized in future processing",
                "Low-performing clips indicate need for better viral moment detection",
                "Platform mismatches suggest need for better platform suggestion algorithms",
                "Engagement patterns guide future content selection and processing"
            ]
        }

def main():
    """Test the enhanced SociaClip AI system"""
    print("🚀 SociaClip AI Enhanced - Complete System Test")
    print("=" * 60)
    
    # Initialize enhanced system
    sociaclip = SociaClipEnhanced()
    
    # Run enhanced workflow
    results = sociaclip.run_enhanced_workflow("fitness")
    
    # Display results
    if results.get("status") == "completed":
        print(f"\n📊 ENHANCED WORKFLOW RESULTS:")
        print(f"   Status: {results['status']}")
        print(f"   Duration: {results.get('duration_seconds', 0)} seconds")
        print(f"   Posts Generated: {len(results.get('final_posts', []))}")
        
        # Video processing results
        if results.get("video_insights"):
            insights = results["video_insights"]
            print(f"   Videos Processed: {insights['processing_summary']['videos_processed']}")
            print(f"   Total Clips: {insights['processing_summary']['total_clips_extracted']}")
            print(f"   Analysis Quality: {insights['processing_summary']['avg_analysis_quality']}/100")
        
        print(f"   🎬 Video Processing: ✅ ENABLED")
        print(f"   🔧 Clips Ready: {results.get('clips_ready', 0)}")

if __name__ == "__main__":
    main()