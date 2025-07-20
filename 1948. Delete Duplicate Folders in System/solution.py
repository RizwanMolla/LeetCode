from collections import defaultdict
class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        root = {}
        for path in paths:
            current = root
            for folder_name in path:
                if folder_name not in current:
                    current[folder_name] = {}
                current = current[folder_name]

        structure_map = defaultdict(list)
        
        to_delete_paths = set()

        def dfs_serialize(node, current_path_tuple):
            if not node:
                return ""

            sorted_child_names = sorted(node.keys())
            
            child_structures = []
            
            for child_name in sorted_child_names:
                child_node = node[child_name]
                child_path_tuple = current_path_tuple + (child_name,)
                child_structure_string = dfs_serialize(child_node, child_path_tuple)
                child_structures.append(f"({child_name}{child_structure_string})")
            
            current_folder_structure = "".join(child_structures)
            
            if not current_folder_structure:
                canonical_structure = "()"
            else:
                canonical_structure = current_folder_structure
                
            structure_map[canonical_structure].append(current_path_tuple)
            
            return canonical_structure

        for top_level_name in sorted(root.keys()):
            top_level_node = root[top_level_name]
            dfs_serialize(top_level_node, (top_level_name,))

        for structure_string, paths_list in structure_map.items():
            if len(paths_list) > 1:
                for path_tuple in paths_list:
                    to_delete_paths.add(path_tuple)
        
        result_paths = []

        def collect_remaining(node, current_path_list):
            if tuple(current_path_list) in to_delete_paths:
                return

            if current_path_list:
                result_paths.append(list(current_path_list))

            for child_name in sorted(node.keys()):
                child_node = node[child_name]
                collect_remaining(child_node, current_path_list + [child_name])

        for top_level_name in sorted(root.keys()):
            top_level_node = root[top_level_name]
            collect_remaining(top_level_node, [top_level_name])

        return result_paths