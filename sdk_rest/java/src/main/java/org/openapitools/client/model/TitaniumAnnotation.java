/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumAnnotation
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-08-17T17:21:02.444709Z[UTC]")
public class TitaniumAnnotation {
  public static final String SERIALIZED_NAME_ANNOTATIONS = "annotations";
  @SerializedName(SERIALIZED_NAME_ANNOTATIONS)
  private Object annotations;

  public static final String SERIALIZED_NAME_ASSET = "asset";
  @SerializedName(SERIALIZED_NAME_ASSET)
  private String asset;

  public static final String SERIALIZED_NAME_ASSET_ID = "assetId";
  @SerializedName(SERIALIZED_NAME_ASSET_ID)
  private String assetId;

  public static final String SERIALIZED_NAME_DATE = "date";
  @SerializedName(SERIALIZED_NAME_DATE)
  private String date;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_MODE = "mode";
  @SerializedName(SERIALIZED_NAME_MODE)
  private String mode;

  public static final String SERIALIZED_NAME_SERVICE = "service";
  @SerializedName(SERIALIZED_NAME_SERVICE)
  private String service;

  public static final String SERIALIZED_NAME_SNAP_TIME = "snapTime";
  @SerializedName(SERIALIZED_NAME_SNAP_TIME)
  private String snapTime;

  public static final String SERIALIZED_NAME_SUB_ASSET = "subAsset";
  @SerializedName(SERIALIZED_NAME_SUB_ASSET)
  private String subAsset;

  public TitaniumAnnotation() { 
  }

  public TitaniumAnnotation annotations(Object annotations) {
    
    this.annotations = annotations;
    return this;
  }

   /**
   * Get annotations
   * @return annotations
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getAnnotations() {
    return annotations;
  }


  public void setAnnotations(Object annotations) {
    this.annotations = annotations;
  }


  public TitaniumAnnotation asset(String asset) {
    
    this.asset = asset;
    return this;
  }

   /**
   * Get asset
   * @return asset
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getAsset() {
    return asset;
  }


  public void setAsset(String asset) {
    this.asset = asset;
  }


  public TitaniumAnnotation assetId(String assetId) {
    
    this.assetId = assetId;
    return this;
  }

   /**
   * Get assetId
   * @return assetId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getAssetId() {
    return assetId;
  }


  public void setAssetId(String assetId) {
    this.assetId = assetId;
  }


  public TitaniumAnnotation date(String date) {
    
    this.date = date;
    return this;
  }

   /**
   * Get date
   * @return date
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDate() {
    return date;
  }


  public void setDate(String date) {
    this.date = date;
  }


  public TitaniumAnnotation description(String description) {
    
    this.description = description;
    return this;
  }

   /**
   * Get description
   * @return description
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDescription() {
    return description;
  }


  public void setDescription(String description) {
    this.description = description;
  }


  public TitaniumAnnotation mode(String mode) {
    
    this.mode = mode;
    return this;
  }

   /**
   * Get mode
   * @return mode
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getMode() {
    return mode;
  }


  public void setMode(String mode) {
    this.mode = mode;
  }


  public TitaniumAnnotation service(String service) {
    
    this.service = service;
    return this;
  }

   /**
   * Get service
   * @return service
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getService() {
    return service;
  }


  public void setService(String service) {
    this.service = service;
  }


  public TitaniumAnnotation snapTime(String snapTime) {
    
    this.snapTime = snapTime;
    return this;
  }

   /**
   * Get snapTime
   * @return snapTime
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getSnapTime() {
    return snapTime;
  }


  public void setSnapTime(String snapTime) {
    this.snapTime = snapTime;
  }


  public TitaniumAnnotation subAsset(String subAsset) {
    
    this.subAsset = subAsset;
    return this;
  }

   /**
   * Get subAsset
   * @return subAsset
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getSubAsset() {
    return subAsset;
  }


  public void setSubAsset(String subAsset) {
    this.subAsset = subAsset;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumAnnotation titaniumAnnotation = (TitaniumAnnotation) o;
    return Objects.equals(this.annotations, titaniumAnnotation.annotations) &&
        Objects.equals(this.asset, titaniumAnnotation.asset) &&
        Objects.equals(this.assetId, titaniumAnnotation.assetId) &&
        Objects.equals(this.date, titaniumAnnotation.date) &&
        Objects.equals(this.description, titaniumAnnotation.description) &&
        Objects.equals(this.mode, titaniumAnnotation.mode) &&
        Objects.equals(this.service, titaniumAnnotation.service) &&
        Objects.equals(this.snapTime, titaniumAnnotation.snapTime) &&
        Objects.equals(this.subAsset, titaniumAnnotation.subAsset);
  }

  @Override
  public int hashCode() {
    return Objects.hash(annotations, asset, assetId, date, description, mode, service, snapTime, subAsset);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumAnnotation {\n");
    sb.append("    annotations: ").append(toIndentedString(annotations)).append("\n");
    sb.append("    asset: ").append(toIndentedString(asset)).append("\n");
    sb.append("    assetId: ").append(toIndentedString(assetId)).append("\n");
    sb.append("    date: ").append(toIndentedString(date)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    mode: ").append(toIndentedString(mode)).append("\n");
    sb.append("    service: ").append(toIndentedString(service)).append("\n");
    sb.append("    snapTime: ").append(toIndentedString(snapTime)).append("\n");
    sb.append("    subAsset: ").append(toIndentedString(subAsset)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("annotations");
    openapiFields.add("asset");
    openapiFields.add("assetId");
    openapiFields.add("date");
    openapiFields.add("description");
    openapiFields.add("mode");
    openapiFields.add("service");
    openapiFields.add("snapTime");
    openapiFields.add("subAsset");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumAnnotation
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumAnnotation.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumAnnotation is not found in the empty JSON string", TitaniumAnnotation.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumAnnotation.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumAnnotation` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("asset") != null && !jsonObj.get("asset").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `asset` to be a primitive type in the JSON string but got `%s`", jsonObj.get("asset").toString()));
      }
      if (jsonObj.get("assetId") != null && !jsonObj.get("assetId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `assetId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("assetId").toString()));
      }
      if (jsonObj.get("date") != null && !jsonObj.get("date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date").toString()));
      }
      if (jsonObj.get("description") != null && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if (jsonObj.get("mode") != null && !jsonObj.get("mode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mode").toString()));
      }
      if (jsonObj.get("service") != null && !jsonObj.get("service").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `service` to be a primitive type in the JSON string but got `%s`", jsonObj.get("service").toString()));
      }
      if (jsonObj.get("snapTime") != null && !jsonObj.get("snapTime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `snapTime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("snapTime").toString()));
      }
      if (jsonObj.get("subAsset") != null && !jsonObj.get("subAsset").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subAsset` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subAsset").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumAnnotation.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumAnnotation' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumAnnotation> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumAnnotation.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumAnnotation>() {
           @Override
           public void write(JsonWriter out, TitaniumAnnotation value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumAnnotation read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumAnnotation given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumAnnotation
  * @throws IOException if the JSON string is invalid with respect to TitaniumAnnotation
  */
  public static TitaniumAnnotation fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumAnnotation.class);
  }

 /**
  * Convert an instance of TitaniumAnnotation to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

